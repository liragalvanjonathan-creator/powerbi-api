from fastapi import FastAPI
from google.cloud import firestore
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "firebase-key.json"

app = FastAPI()

db = firestore.Client()

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