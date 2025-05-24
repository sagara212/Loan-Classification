import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    "Create a test client for the FastAPI app"
    with TestClient(app) as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'text/html' in response.headers['content-type'].lower()
    assert 'loan' in response.text.lower()

@pytest.mark.parametrize("payload", [
    {
        "person_age": 22.0,
        "person_gender": "female",
        "person_education": "Master",
        "person_income": 71948.0,
        "person_emp_exp": 0,
        "person_home_ownership": "RENT",
        "loan_amnt": 35000.0,
        "loan_intent": "PERSONAL",
        "loan_int_rate": 16.02,
        "loan_percent_income": 0.49,
        "cb_person_cred_hist_length": 3.0,
        "credit_score": 561,
        "previous_loan_defaults_on_file": "No"
    },
    {
        "person_age": 21.0,
        "person_gender": "female",
        "person_education": "High School",
        "person_income": 12282.0,
        "person_emp_exp": 0,
        "person_home_ownership": "OWN",
        "loan_amnt": 1000.0,
        "loan_intent": "EDUCATION",
        "loan_int_rate": 11.14,
        "loan_percent_income": 0.08,
        "cb_person_cred_hist_length": 2.0,
        "credit_score": 504,
        "previous_loan_defaults_on_file": "Yes"
    },
    {
        "person_age": 26.0,
        "person_gender": "female",
        "person_education": "Bachelor",
        "person_income": 93471.0,
        "person_emp_exp": 1,
        "person_home_ownership": "RENT",
        "loan_amnt": 35000.0,
        "loan_intent": "EDUCATION",
        "loan_int_rate": 12.42,
        "loan_percent_income": 0.37,
        "cb_person_cred_hist_length": 3.0,
        "credit_score": 701,
        "previous_loan_defaults_on_file": "No"
    }
])
def test_predict_with_valid_samples(client, payload):
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] in ["disetujui", "ditolak"]

def test_predict_missing_field(client):
    payload = {
        # missing 'person_age'
        "person_gender": "female",
        "person_education": "Bachelor",
        "person_income": 93471.0,
        "person_emp_exp": 1,
        "person_home_ownership": "RENT",
        "loan_amnt": 35000.0,
        "loan_intent": "EDUCATION",
        "loan_int_rate": 12.42,
        "loan_percent_income": 0.37,
        "cb_person_cred_hist_length": 3.0,
        "credit_score": 701,
        "previous_loan_defaults_on_file": "No"
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422  # Unprocessable Entity due to missing field
