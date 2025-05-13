

# 🏦 Loan Classification ML Project

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python) ![FastAPI](https://img.shields.io/badge/FastAPI-API%20Framework-green?logo=fastapi) ![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker) ![Deployed](https://img.shields.io/badge/Deployed-Railway-green?logo=railway)

## 🚀 Overview

This project aims to classify whether a loan applicant is eligible for **loan approval** using **machine learning algorithms**. The model predicts loan approval status based on the applicant’s **financial profile** and **credit history**.

🔗 **Live App:** [Loan Classification Web App](https://loan-classification-production.up.railway.app/)

---

## 🧠 Features

* Clean and intuitive **web interface**.
* End-to-end ML pipeline:

  * Data preprocessing & cleaning
  * Model training & evaluation using LightGBM
  * REST API for model inference using **FastAPI**
* Dockerized for smooth and scalable deployment.
* Hosted live via **Railway**.

---

## 📊 Machine Learning

* **Model Used**: LightGBM
* **Target Variable**: `Loan_Status` (Approved / Not Approved)
* **Input Features**: Income, Employment Status, Credit History, Loan Amount, and more.
* **Evaluation Metrics**: Accuracy, Precision, Recall, F1-Score

---

## 🧰 Tech Stack

| Purpose             | Tech                   |
| ------------------- | ---------------------- |
| Programming         | Python                 |
| API Framework       | FastAPI                |
| Deployment          | Docker, Railway        |
| Data Processing     | Pandas, NumPy          |
| Model Training      | LightGBM, scikit-learn |
| Model Serialization | joblib                 |

---

## 🖥️ Local Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/username/loan-classification.git
cd loan-classification

# 2. Build the Docker image
docker build -t loan-classifier .

# 3. Run the container
docker run -p 8000:8000 loan-classifier
```

The app will be available at: [http://localhost:8000/docs](http://localhost:8000/docs)
(*FastAPI provides an interactive Swagger UI for testing your API!*)

---

## 🌐 Deployment

This app is deployed on **Railway**, an easy-to-use cloud platform that builds directly from the Dockerfile and hosts the FastAPI application online.

---

## 📸 Preview

![image](https://github.com/user-attachments/assets/c4f1ecd1-4465-4186-b626-efad1c881a3a)

![image](https://github.com/user-attachments/assets/097e9858-3620-4e35-b8e4-66af6d9e07ab)



---


