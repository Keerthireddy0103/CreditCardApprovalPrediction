from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load model
model = None
model_path = "model.pkl"

if os.path.exists(model_path):
    model = joblib.load(model_path)

    print("Model loaded successfully")
    print("Number of features:", model.n_features_in_)

    try:
        print("Feature names:")
        print(model.feature_names_in_)
    except:
        print("Feature names are not available.")

else:
    print("Warning: model.pkl not found.")
    print("Warning: model.pkl not found. Train model first.")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read form inputs
        gender = int(request.form["gender"])
        car = int(request.form["car"])
        reality = int(request.form["reality"])
        child_num = int(request.form["child_num"])
        income_total = float(request.form["income_total"])
        income_type = int(request.form["income_type"])
        education_type = int(request.form["education_type"])
        family_type = int(request.form["family_type"])
        housing_type = int(request.form["housing_type"])
        days_birth = int(request.form["days_birth"])
        days_employed = int(request.form["days_employed"])
        flag_mobil = int(request.form["flag_mobil"])
        work_phone = int(request.form["work_phone"])
        phone = int(request.form["phone"])
        email = int(request.form["email"])
        occupation_type = int(request.form["occupation_type"])
        family_members = int(request.form["family_members"])

        features = np.array([[
            gender, car, reality, child_num, income_total,
            income_type, education_type, family_type, housing_type,
            days_birth, days_employed, flag_mobil, work_phone,
            phone, email, occupation_type, family_members
        ]])

        if model is None:
            return render_template(
                "result.html",
                prediction_text="Model file not found. Please train the model first.",
                result_class="reject"
            )

        prediction = model.predict(features)[0]

        # Adjust this if your model label meaning is reversed
        if prediction == 1:
            result = "Credit Card Approved"
            result_class = "approve"
        else:
            result = "Credit Card Rejected"
            result_class = "reject"

        return render_template(
            "result.html",
            prediction_text=result,
            result_class=result_class
        )

    except Exception as e:
        return render_template(
            "result.html",
            prediction_text=f"Error: {str(e)}",
            result_class="reject"
        )

if __name__ == "__main__":
    app.run(debug=True)