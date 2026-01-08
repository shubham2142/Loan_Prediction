from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load trained advanced model

model = joblib.load("model/best_loan_model.pkl")
# Agar scaler use kiya hai to uncomment karo
# scaler = joblib.load("model/scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    try:
        # ================================
        # Get input values from form
        # ================================
        Gender = int(request.form["Gender"])
        Married = int(request.form["Married"])
        Dependents = int(request.form["Dependents"])
        Education = int(request.form["Education"])
        Self_Employed = int(request.form["Self_Employed"])
        ApplicantIncome = float(request.form["ApplicantIncome"])
        CoapplicantIncome = float(request.form["CoapplicantIncome"])
        LoanAmount = float(request.form["LoanAmount"])
        Loan_Amount_Term = float(request.form["Loan_Amount_Term"])
        Credit_History = float(request.form["Credit_History"])
        Property_Area = int(request.form["Property_Area"])

        # ================================
        # Feature Engineering (ADVANCED)
        # ================================
        TotalIncome = ApplicantIncome + CoapplicantIncome
        Loan_Income_Ratio = LoanAmount / TotalIncome if TotalIncome != 0 else 0

        # ================================
        # Create input array (ORDER MATTERS)
        # ================================
        input_data = np.array([[
            Gender,
            Married,
            Dependents,
            Education,
            Self_Employed,
            ApplicantIncome,
            CoapplicantIncome,
            LoanAmount,
            Loan_Amount_Term,
            Credit_History,
            Property_Area,
            TotalIncome,
            Loan_Income_Ratio
        ]])

        # Agar scaler use kiya hai
        # input_data = scaler.transform(input_data)

        # ================================
        # Prediction
        # ================================
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        risk_score = int(probability * 100)

        # ================================
        # Risk Category
        # ================================
        if risk_score < 30:
            risk_category = "Low Risk"
        elif risk_score < 60:
            risk_category = "Medium Risk"
        else:
            risk_category = "High Risk"

        # ================================
        # Final Result
        # ================================
        result = "APPROVED ✅" if prediction == 1 else "REJECTED ❌"

        return render_template(
            "result.html",
            result=result,
            risk_score=risk_score,
            risk_category=risk_category
        )

    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
