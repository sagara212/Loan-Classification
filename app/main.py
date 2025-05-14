from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import joblib
import logging
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Inisialisasi FastAPI
app = FastAPI()

# Static file
BASE_DIR = os.path.dirname(__file__)
static_path = os.path.join(BASE_DIR, "static")

if not os.path.exists(static_path):
    os.makedirs(static_path)  # Opsional: buat folder jika tidak ada

app.mount("/static", StaticFiles(directory=static_path), name="static")

# Global pipeline
pipeline = None

@app.on_event("startup")
def load_model():
    global pipeline
    model_path = os.getenv("MODEL_PATH", os.path.join(BASE_DIR, "pipeline.pkl"))

    if not os.path.isfile(model_path):
        logging.error(f"File pipeline tidak ditemukan: {model_path}")
        raise RuntimeError("File pipeline tidak ditemukan")

    try:
        pipeline = joblib.load(model_path)
        logging.info("Pipeline berhasil dimuat")
    except Exception as e:
        logging.error(f"Gagal load pipeline: {e}")
        raise RuntimeError("Gagal memuat pipeline")


# Kolom input
NUMERIC_FEATURES = [
    "person_age",
    "person_income",
    "person_emp_exp",
    "loan_amnt",
    "loan_int_rate",
    "loan_percent_income",
    "cb_person_cred_hist_length",
    "credit_score",
]

CATEGORICAL_FEATURES = [
    "person_education",
    "person_home_ownership",
    "loan_intent",
    "previous_loan_defaults_on_file",
    "person_gender"
]

class features(BaseModel):
    person_age: float
    person_gender: str
    person_education: str
    person_income: float
    person_emp_exp: float
    person_home_ownership: str
    loan_amnt: float
    loan_intent: str
    loan_int_rate: float
    loan_percent_income: float
    cb_person_cred_hist_length: float
    credit_score: float
    previous_loan_defaults_on_file: str

# Homepage
@app.get("/")
def read_index():
    index_path = os.path.join(static_path, "index.html")
    if not os.path.exists(index_path):
        raise HTTPException(status_code=404, detail="index.html tidak ditemukan")
    return FileResponse(index_path)

# Endpoint prediksi
@app.post("/predict")
def predict(request: features):
    global pipeline
    if pipeline is None:
        raise HTTPException(status_code=500, detail="Pipeline belum dimuat")

    try:
        data = request.dict()
        logging.info(f"Data diterima: {data}")  # Tambahkan logging

        df = pd.DataFrame([data])
        df = df[NUMERIC_FEATURES + CATEGORICAL_FEATURES]

        logging.info(f"Dataframe untuk prediksi:\n{df}")

        pred = pipeline.predict(df)[0]
        status = "disetujui" if pred == 1 else "ditolak"
        return {"status": status}
    
    except Exception as e:
        logging.error(f"Error saat prediksi: {e}")
        raise HTTPException(status_code=500, detail="Gagal memproses prediksi")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
