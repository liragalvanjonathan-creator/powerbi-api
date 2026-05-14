from fastapi import FastAPI
from google.cloud import firestore
from google.oauth2 import service_account

app = FastAPI()

# 🔐 conexión Firebase
try:
    credentials = service_account.Credentials.from_service_account_file(
        "firebase-key.json"
    )
    db = firestore.Client(credentials=credentials)
except Exception as e:
    db = None
    error_message = str(e)

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/production")
def get_production():
    if db is None:
        return {"error": "DB not initialized", "details": error_message}

    try:
        docs = db.collection("production").stream()
        return [doc.to_dict() for doc in docs]
    except Exception as e:
        return {"error": str(e)}

@app.get("/preparation")
def get_preparation():
    if db is None:
        return {"error": "DB not initialized", "details": error_message}

    try:
        docs = db.collection("preparation").stream()
        return [doc.to_dict() for doc in docs]
    except Exception as e:
        return {"error": str(e)}
