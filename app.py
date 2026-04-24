"""
Job Salary Prediction - Flask Web App
======================================
Run: python app.py
Visit: http://localhost:5000
"""

from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# ── Load model and encoders ────────────────────────────────────────────────────
MODEL_PATH   = "../models/salary_model.pkl"
ENCODER_PATH = "../models/label_encoders.pkl"

model = None
label_encoders = None

def load_model():
    global model, label_encoders
    if os.path.exists(MODEL_PATH) and os.path.exists(ENCODER_PATH):
        model = joblib.load(MODEL_PATH)
        label_encoders = joblib.load(ENCODER_PATH)
        print("✅ Model loaded successfully")
    else:
        print("⚠️  Model not found. Run train_model.py first.")

# ── Options for dropdowns ──────────────────────────────────────────────────────
OPTIONS = {
    "job_title": ["AI Engineer", "Backend Developer", "Business Analyst",
                  "Cloud Architect", "Cybersecurity Analyst", "Data Analyst",
                  "Data Scientist", "DevOps Engineer", "Frontend Developer",
                  "Full Stack Developer", "ML Engineer", "Product Manager"],
    "education_level": ["Bachelor's", "Master's", "PhD", "Associate's", "High School"],
    "industry": ["Finance", "Healthcare", "Retail", "Education", "Government",
                 "Energy", "Media", "Manufacturing", "Technology", "Consulting"],
    "company_size": ["Small", "Medium", "Large", "Startup", "Enterprise"],
    "location": ["Austin", "Boston", "Chicago", "Los Angeles", "Miami",
                 "New York", "San Francisco", "Seattle", "Toronto", "London"],
    "remote_work": ["Remote", "Hybrid", "On-site"]
}

@app.route("/")
def index():
    return render_template("index.html", options=OPTIONS)

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded. Run train_model.py first."}), 500

    data = request.get_json()
    CATEGORICAL_COLS = ["job_title", "education_level", "industry",
                        "company_size", "location", "remote_work"]
    FEATURE_ORDER = ["job_title", "experience_years", "education_level",
                     "skills_count", "industry", "company_size",
                     "location", "remote_work", "certifications"]

    try:
        features = []
        for feat in FEATURE_ORDER:
            val = data[feat]
            if feat in CATEGORICAL_COLS:
                val = label_encoders[feat].transform([val])[0]
            else:
                val = float(val)
            features.append(val)

        prediction = model.predict([features])[0]
        return jsonify({"salary": f"${prediction:,.0f}"})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    load_model()
    app.run(debug=True)
