# Sample Code
# How to Push/Add 1 data to Firebase WITHOUT authentication

from firebase import firebase
# init
firebase = firebase.FirebaseApplication('YOUR-FIREBASE-PROJECT-URL', authentication=None)
# push data
mahasiswa = {
	"nama": "Joni",
	"asal": "Gresik",
	"umur": "20",
	"hobi": ["Begadang"]
}
result = firebase.post('/YOUR-COLLECTION', mahasiswa)
print result