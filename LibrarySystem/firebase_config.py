import firebase_admin
from firebase_admin import credentials, db
import os

# Load the Firebase credentials JSON
cred = credentials.Certificate(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'firebase-private-key.json'))

# Initialize Firebase
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://librarymanagement-f296d-default-rtdb.firebaseio.com/'  # Replace with your Firebase Realtime Database URL
})