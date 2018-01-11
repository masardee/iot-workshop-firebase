# Sample Code
# How to Push/Add 1 data to Firebase WITHOUT authentication

import pyrebase

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
mahasiswa = {
	"nama": "Rara",
	"asal": "Surabaya",
	"umur": "19",
	"hobi": ["Berenang"]
}
result = db.child('mahasiswacollection').push(mahasiswa)
print result