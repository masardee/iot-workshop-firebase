# Firebase Starter Project #

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
collection_name = "mahasiswacollection"

# Init
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Push data
def push_data():
    global db
    mahasiswa = {
        "nama": "Rara",
        "asal": "Surabaya",
        "umur": "19",
        "hobi": ["Berenang"]
    }
    result = db.child(collection_name).push(mahasiswa)
    print result

# Retrieve data
def get_list():
    global db, collection_name
    result = db.child(collection_name).get()
    print (json.dumps(result.val(), indent=4))

# Filter data
def get_list_filter(kota):
    global db, collection_name
    result = db.child(collection_name).order_by_child('asal').equal_to(kota).get()
    # Print
    if len(result.pyres) > 0:
        print(json.dumps(result.val(), indent=4))
    else:
        print("No Result!")

# Stream
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

def stream():
    global db
    db.child(collection_name).stream(stream_handler)

# Run
stream()
print("Hi... I run after stream initiated!")