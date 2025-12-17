import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

firebase_creds_json = os.getenv("FIREBASE_SERVICE_ACCOUNT")

if not firebase_creds_json:
    raise ValueError("FIREBASE_SERVICE_ACCOUNT env variable not set")

firebase_creds = json.loads(firebase_creds_json)

# initialize firebase only once
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_creds)
    firebase_admin.initialize_app(cred)

db = firestore.client()
