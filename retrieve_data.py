# Sample Code
# How to Retrieve Data from Firebase WITHOUT authentication

import pyrebase

config = {
    "apiKey" : False,
    "authDomain": False,
    "databaseURL": "https://iot-project-11a31.firebaseio.com/",
    "storageBucket": False
}

# Init
firebase = pyrebase.initialize_app(config)
db = firebase.database()
# Retreive
result = db.child('mahasiswacollection').get()
print (result.val())