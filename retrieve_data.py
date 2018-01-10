# Sample Code
# How to Retrieve Data from Firebase WITHOUT authentication

from firebase import firebase

# Init
firebase = firebase.FirebaseApplication('YOUR-FIREBASE-PROJECT-URL', authentication=None)
# Retreive
result = firebase.get('/YOUR-COLLECTION', None)
print result