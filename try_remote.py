# Import...
import pyrebase
import json

# Config
config = {
    "apiKey" : False,
    "authDomain": False,
    "databaseURL": "https://iot-project-11a31.firebaseio.com/",
    "storageBucket": False
}
collection_name = "IOT_REMOTE"

# Init
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# DEVICE INFO
device = {
    "owner": "Ardi",
    "email": "ardi.imawan@dot.co.id"
}
device_name = ''

# Register Device to Firebase
def register():
    global db, device, device_name
    result = db.child(collection_name).push(device)
    device_name = result['name']
    print(json.dumps(result, indent=4))

# Listen
stream_counter = 0
def stream_handler(message):
    global stream_counter
    if stream_counter > 0:
        print(message["event"])
        print(message["path"])
        print(json.dumps(message["data"], indent=4))
    else:
        print("Listener just started....")
    stream_counter+=1

def listen():
    global db, collection_name
    print("Listen to Device " + device_name)
    db.child(collection_name + '/' + device_name + '/commands').stream(stream_handler)

# Run
register()
listen()