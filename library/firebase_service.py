import pyrebase
from django.conf import settings

firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)
db = firebase.database()  # Realtime Database access