# Sample Code
# How to Retrieve Data from Firebase WITHOUT authentication
# Will be printed in beauty format

import pyrebase
import json

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
# Print
print(json.dumps(result.val(), indent=4))