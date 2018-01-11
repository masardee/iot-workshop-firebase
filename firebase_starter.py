# Sample Code
# How to Push/Add/Get data from/to Firebase WITHOUT authentication

# Import...
import pyrebase

# Config
config = {
    "apiKey" : False,
    "authDomain": False,
    "databaseURL": "https://iot-project-11a31.firebaseio.com/",
    "storageBucket": False
}

# Init
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Push data

# Retrieve data

# Filter data

# Stream

# Run
print("Hi... this is a starter file")