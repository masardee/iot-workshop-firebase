# Sample Code
# How to Push/Add/Get data from/to Firebase WITHOUT authentication

import pyrebase
import json

# Config
config = {
    "apiKey" : False,
    "authDomain": False,
    "databaseURL": "https://iot-project-11a31.firebaseio.com/",
    "storageBucket": False
}

# init
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# push data
def push_data():
    global db
    mahasiswa = {
        "nama": "Rara",
        "asal": "Surabaya",
        "umur": "19",
        "hobi": ["Berenang"]
    }
    result = db.child('mahasiswacollection').push(mahasiswa)
    print result

# retrieve data
def get_list():
    global db
    result = db.child('mahasiswacollection').get()
    print (result.val())

# filter data
def get_list_filter():
    global db
    result = db.child('mahasiswacollection').order_by_child('asal').equal_to('Gresik').get()
    # Print
    if len(result.pyres) > 0:
        print(json.dumps(result.val(), indent=4))
    else:
        print("No Result!")

# stream
def stream():
    global db
    db.child('mahasiswacollection').stream(stream_handler)

stream_counter = 0
def stream_handler(message):
    global stream_counter
    if stream_counter > 0:
        print(message["event"]) # put
        print(message["path"]) # /-K7yGTTEp7O549EzTYtI
        print(json.dumps(message["data"], indent=4))
    else:
        print("Stream started....")
    stream_counter+=1

stream()