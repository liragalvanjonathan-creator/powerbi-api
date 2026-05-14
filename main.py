from fastapi import FastAPI
from google.cloud import firestore
from google.oauth2 import service_account

app = FastAPI()

# 🔐 conexión correcta a Firebase
credentials = service_account.Credentials.from_service_account_file(
    "firebase-key.json"
)

db = firestore.Client(credentials=credentials)

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/production")
def get_production():
    docs = db.collection("production").stream()
    return [doc.to_dict() for doc in docs]

@app.get("/preparation")
def get_preparation():
    docs = db.collection("preparation").stream()
    return [doc.to_dict() for doc in docs]