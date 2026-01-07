from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model/loan_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = [
        int(request.form["Gender"]),
        int(request.form["Married"]),
        int(request.form["Dependents"]),
        int(request.form["Education"]),
        int(request.form["Self_Employed"]),
        float(request.form["ApplicantIncome"]),
        float(request.form["CoapplicantIncome"]),
        float(request.form["LoanAmount"]),
        float(request.form["Loan_Amount_Term"]),
        float(request.form["Credit_History"]),
        int(request.form["Property_Area"])
    ]

    input_data = np.array(data).reshape(1, -1)

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    risk_score = int(probability * 100)

    result = "APPROVED ✅" if prediction == 1 else "REJECTED ❌"

    return render_template(
        "result.html",
        result=result,
        risk_score=risk_score
    )

if __name__ == "__main__":
    app.run(debug=True)
