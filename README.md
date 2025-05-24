

# 🏦 Loan Classification ML Project

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python) ![FastAPI](https://img.shields.io/badge/FastAPI-API%20Framework-green?logo=fastapi) ![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker) ![Deployed](https://img.shields.io/badge/Deployed-Railway-green?logo=railway) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?logo=scikit-learn&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?logo=numpy&logoColor=white)

## 🚀 Project Overview

This project aims to classify whether a loan applicant is eligible for **loan approval** using **machine learning algorithms**. 📈 The model predicts loan approval status based on the applicant’s **financial profile** and **credit history**. 💳

🔗 **Live App:** [Loan Classification Web App](https://loan-classification-production.up.railway.app/) 🌐

---

## 🎯 Problem Statement
Many financial institutions struggle with efficiently and accurately assessing loan applications. This project aims to develop a reliable machine learning model to automate the loan approval process, reducing manual effort and improving decision-making consistency.

---

## ✨ Key Features

* ✅ Clean and intuitive **web interface**.
* 🔄 End-to-end ML pipeline:

  * 🧹 Data preprocessing & cleaning
  * 🏋️ Model training & evaluation using LightGBM
  * 🚀 FastAPI REST API for model inference
* 🐳 Dockerized for smooth and scalable deployment.
* ☁️ Hosted live via **Railway** platform.

---

## 🤖 Machine Learning Model

* **Model Used**: LightGBM 💡
* **Target Variable**: `Loan_Status` (Approved / Not Approved) 🎯
* **Key Input Features**: Applicant's income, employment status, credit history, loan amount. 📝
* **Evaluation Metrics**: Accuracy, Precision, Recall, F1-Score. 📊

---

## 🛠️ Tech Stack

| Category            | Technology             |
| ------------------- | ---------------------- |
| Programming Language| Python 3.10            |
| API Framework       | FastAPI                |
| Deployment          | Docker, Railway        |
| Data Manipulation   | Pandas, NumPy          |
| ML Model Training   | LightGBM, scikit-learn |
| Model Serialization | joblib                 |

---

## 🌟 Key Learnings
- Gained hands-on experience with the end-to-end machine learning workflow, from data preprocessing to deployment.
- Learned the importance of feature engineering and model evaluation in building effective predictive models.
- Explored the benefits of using FastAPI for creating efficient and scalable APIs.
- Understood the convenience of Docker and Railway for containerization and cloud deployment.

---

## 💻 Local Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/username/loan-classification.git # TODO: Update with actual repository URL
cd loan-classification

# 2. Build the Docker image
docker build -t loan-classifier .

# 3. Run the Docker container
docker run -p 8000:8000 loan-classifier
```

The application will be accessible at: `http://localhost:8000/docs`
(FastAPI's interactive Swagger UI is great for API testing!)

---

## ☁️ Deployment

This application is deployed on **Railway** 🚂, a user-friendly cloud platform that automatically builds from the Dockerfile and hosts the FastAPI application. 🚀

---

## 🚀 Future Improvements
- [ ] Experiment with other classification algorithms (e.g., XGBoost, RandomForest) to compare performance.
- [ ] Implement more advanced feature engineering techniques.
- [ ] Add user authentication and a dashboard for admin users.
- [ ] Expand the test suite to include more comprehensive API and model tests.

---

## 🖼️ Application Preview

<!-- TODO: Review header image. Consider creating a project logo. -->
<p align="center">
  <img src="https://github.com/user-attachments/assets/c4f1ecd1-4465-4186-b626-efad1c881a3a" alt="App Screenshot 1" width="70%">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/097e9858-3620-4e35-b8e4-66af6d9e07ab" alt="App Screenshot 2" width="70%">
</p>

---
