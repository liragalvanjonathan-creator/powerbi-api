from fastapi import FastAPI
from google.cloud import firestore
from google.oauth2 import service_account

app = FastAPI()

# 🔐 Conexión segura a Firebase (Render compatible)
try:
    credentials = service_account.Credentials.from_service_account_file(
        "firebase-key.json"
    )
    db = firestore.Client(credentials=credentials)
except Exception as e:
    db = None
    error_message = str(e)

# ✅ Endpoint base (para verificar que todo está vivo)
@app.get("/")
def home():
    return {"status": "ok"}

# ✅ Endpoint PRODUCTION
@app.get("/production")
def get_production():
    if db is None:
        return {"error": "DB not initialized", "details": error_message}

    try:
        docs = db.collection("production").stream()
        data = []

        for doc in docs:
            d = doc.to_dict()

            # 🔧 Convertir timestamp a string
            if "timestamp" in d:
                try:
                    d["timestamp"] = d["timestamp"].isoformat()
                except:
                    pass

            data.append(d)

        return data

    except Exception as e:
        return {"error": str(e)}

# ✅ Endpoint PREPARATION
@app.get("/preparation")
def get_preparation():
    if db is None:
        return {"error": "DB not initialized", "details": error_message}

    try:
        docs = db.collection("preparation").stream()
        data = []

        for doc in docs:
            d = doc.to_dict()

            # 🔧 Convertir timestamp a string
            if "timestamp" in d:
                try:
                    d["timestamp"] = d["timestamp"].isoformat()
                except:
                    pass

            data.append(d)

        return data

    except Exception as e:
        return {"error": str(e)}