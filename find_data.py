# Sample Code
# How to Retrieve Data with FILTER

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
result = db.child('mahasiswacollection').order_by_child('asal').equal_to('Gresik').get()
# Print
if len(result.pyres) > 0:
    print(json.dumps(result.val(), indent=4))
else:
    print("No Result!")