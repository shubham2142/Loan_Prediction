# 🏦 Loan Approval System with Risk Scoring

An end-to-end **Machine Learning + Flask** web application that predicts **loan approval status** and calculates an applicant **risk score (0–100%)** based on financial and personal details.

---

## 📌 Project Overview

This project demonstrates the complete lifecycle of a machine learning system:

* Data preprocessing and feature engineering
* Training and evaluation of classification models
* Model selection and persistence
* Deployment as a **Flask web application** with a clean, user-friendly UI

The application predicts whether a loan should be **Approved or Rejected** and provides a **risk score** derived from model prediction probability to help interpret applicant risk.

---

## 🧠 Problem Statement

Predict loan approval using applicant information such as income, credit history, education, employment type, and property area.

**Problem Type:**

* Supervised Machine Learning
* Binary Classification

**Target Variable:**

* `Loan_Status` → Approved / Rejected

---

## 📊 Dataset

* **Source:** Loan Approval Dataset (CSV)

* **Records:** ~600 loan applications

* **Features:**

  * Gender
  * Married
  * Dependents
  * Education
  * Self_Employed
  * ApplicantIncome
  * CoapplicantIncome
  * LoanAmount
  * Loan_Amount_Term
  * Credit_History
  * Property_Area

* **Target:**

  * `Loan_Status`

Dataset file location:

```
data/Loan-Approval-Prediction.csv
```

---

## ⚙️ Machine Learning Pipeline

1. Data loading and inspection
2. Missing value handling
3. Encoding of categorical variables
4. Feature engineering

   * Total Income
   * Loan–Income Ratio
5. Train–test split
6. Model training

   * Logistic Regression
   * Random Forest
7. Hyperparameter tuning using `GridSearchCV`
8. Model evaluation

   * Accuracy
   * ROC-AUC
   * Confusion Matrix
9. Model persistence using `joblib`
10. Deployment with Flask

---

## 🧪 Models Used

| Model               | Purpose                                 |
| ------------------- | --------------------------------------- |
| Logistic Regression | Baseline binary classifier              |
| Random Forest       | Ensemble model for improved performance |
| Tuned Random Forest | Best-performing model (final)           |

Saved model artifacts:

* `logistic_model.pkl`
* `best_loan_model.pkl`
* `scaler.pkl`

---

## 📈 Risk Scoring Logic

* The **risk score (0–100%)** is derived from the model's predicted probability.
* Higher probability of rejection → higher risk score.

**Risk Categories:**

* **Low Risk:** High approval probability
* **Medium Risk:** Moderate approval probability
* **High Risk:** Low approval probability

---

## 🌐 Web Application Features

* Loan application input form
* Real-time prediction results
* Loan decision: **Approved / Rejected**
* Risk score visualization
* Risk category (Low / Medium / High)
* Clean and responsive user interface
* Flask-based backend

---

## 🗂️ Project Structure

```
Loan_Approval/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   └── Loan-Approval-Prediction.csv
│
├── notebooks/
│   └── loan_model_training.ipynb
│
├── model/
│   ├── logistic_model.pkl
│   ├── best_loan_model.pkl
│   └── scaler.pkl
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
```

---

## ▶️ How to Run the Project (Windows)

```powershell
# 1️⃣ Clone the repository
git clone https://github.com/shubham2142/Loan_Prediction.git

# 2️⃣ Create a virtual environment
python -m venv venv

# 3️⃣ Activate the virtual environment
venv\Scripts\activate

# 4️⃣ Install dependencies
pip install -r requirements.txt

# 5️⃣ Run the Flask application
python app.py

# 6️⃣ Open the app in your browser
http://127.0.0.1:5000
```

---

## 📌 Notes

* Ensure the `model/` directory contains all trained model files before running the app.
* If you retrain models using `notebooks/loan_model_training.ipynb`, the notebook saves updated artifacts into the `model/` folder using `joblib`.
* Logistic Regression uses `StandardScaler`; Random Forest does not require scaling.

---

## 📈 Sample Output

* **Loan Decision:** Approved / Rejected
* **Risk Score:** 0–100%
* **Risk Category:** Low / Medium / High

---

## 🤝 Contribution & Contact

Contributions are welcome.

* Open an issue for bug reports or feature requests
* Submit a pull request for improvements

For questions, please refer to the original GitHub repository or raise an issue there.
