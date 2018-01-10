# Sample Code
# How to Retrieve Data from Firebase WITHOUT authentication
# Will be printed in beauty format

from firebase import firebase
import json

# init
firebase = firebase.FirebaseApplication('https://iot-project-11a31.firebaseio.com/', authentication=None)
# retrieve data
result = firebase.get('/mahasiswacollection/', None)
print json.dumps(result, indent=4, sort_keys=True)