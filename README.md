# 🏦 Loan Approval System with Risk Scoring

An end-to-end **Machine Learning + Flask** web application that predicts
loan approval status and calculates applicant risk score based on
financial and personal details.

---

## 📌 Project Overview

This project uses **Machine Learning classification models** to determine
whether a loan application should be **Approved or Rejected**.
Additionally, a **risk score (0–100%)** is generated using prediction
probability to help understand applicant risk level.

The trained model is deployed using a **Flask web application** with a
clean and user-friendly interface.

---

## 🧠 Problem Statement

To predict loan approval status using applicant data such as income,
credit history, education, employment type, and property area.

**Type of Problem:**  
- Supervised Machine Learning  
- Binary Classification

---

## 📊 Dataset

- Source: Loan Approval Dataset (CSV)
- Records: ~600 loan applications
- Features:
  - Gender
  - Married
  - Dependents
  - Education
  - Self Employed
  - Applicant Income
  - Coapplicant Income
  - Loan Amount
  - Loan Amount Term
  - Credit History
  - Property Area

- Target:
  - Loan_Status (Approved / Rejected)

---

## ⚙️ Machine Learning Pipeline

1. Data collection and loading  
2. Data cleaning and missing value handling  
3. Encoding categorical variables  
4. Feature engineering (Total Income, Loan-Income Ratio)  
5. Train–test split  
6. Model training (Logistic Regression, Random Forest)  
7. Hyperparameter tuning (GridSearchCV)  
8. Model evaluation (Accuracy, ROC-AUC, Confusion Matrix)  
9. Model saving using `joblib`  
10. Deployment using Flask  

---

## 🧪 Models Used

| Model | Description |
|-----|------------|
| Logistic Regression | Baseline binary classification model |
| Random Forest | Advanced ensemble model |
| Tuned Random Forest | Best performing model |

---

## 🌐 Web Application Features

- Loan application form
- Real-time prediction
- Risk score calculation
- Risk category (Low / Medium / High)
- Clean & responsive UI
- Flask-based backend

---

## 🗂️ Project Structure

Loan_Approval/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│ └── Loan-Approval-Prediction.csv
│
├── notebooks/
│ └── loan_model_training.ipynb
│
├── model/
│ ├── logistic_model.pkl
│ ├── best_loan_model.pkl
│ └── scaler.pkl
│
├── templates/
│ ├── index.html
│ └── result.html
│
└── static/
└── style.css


---

## ▶️ How to Run the Project

```bash

1️⃣ Clone Repository
git clone hhttps://github.com/shubham2142/Loan_Prediction
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Flask App
python app.py
5️⃣ Open Browser
http://127.0.0.1:5000

📈 Sample Output
Loan Decision: Approved / Rejected
Risk Score: 0–100%
Risk Category: Low / Medium / High