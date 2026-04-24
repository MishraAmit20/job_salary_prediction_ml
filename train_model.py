"""
Job Salary Prediction - Model Training Script
==============================================
Trains a Random Forest Regressor to predict job salaries
based on experience, education, skills, industry, location, and more.
"""

import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import warnings
warnings.filterwarnings("ignore")

# ── Paths ──────────────────────────────────────────────────────────────────────
DATA_PATH   = "data/job_salary_prediction_dataset.csv"
MODEL_PATH  = "models/salary_model.pkl"
ENCODER_PATH = "models/label_encoders.pkl"

# ── 1. Load Data ───────────────────────────────────────────────────────────────
print("📂 Loading dataset...")
df = pd.read_csv(DATA_PATH)
print(f"   Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")

# ── 2. Preprocessing ───────────────────────────────────────────────────────────
print("\n🔧 Preprocessing...")

CATEGORICAL_COLS = ["job_title", "education_level", "industry",
                    "company_size", "location", "remote_work"]

label_encoders = {}
for col in CATEGORICAL_COLS:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    label_encoders[col] = le
    print(f"   Encoded '{col}' → {len(le.classes_)} categories")

# ── 3. Features & Target ───────────────────────────────────────────────────────
FEATURE_COLS = ["job_title", "experience_years", "education_level",
                "skills_count", "industry", "company_size",
                "location", "remote_work", "certifications"]

X = df[FEATURE_COLS]
y = df["salary"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\n📊 Train: {len(X_train):,} | Test: {len(X_test):,}")

# ── 4. Train Model ─────────────────────────────────────────────────────────────
print("\n🚀 Training Random Forest Regressor...")
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=20,
    min_samples_split=5,
    min_samples_leaf=2,
    n_jobs=-1,
    random_state=42
)
model.fit(X_train, y_train)
print("   Training complete ✅")

# ── 5. Evaluate ────────────────────────────────────────────────────────────────
print("\n📈 Evaluating on test set...")
y_pred = model.predict(X_test)

mae  = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2   = r2_score(y_test, y_pred)

print(f"   MAE  : ${mae:,.0f}")
print(f"   RMSE : ${rmse:,.0f}")
print(f"   R²   : {r2:.4f}")

# ── 6. Feature Importance ──────────────────────────────────────────────────────
print("\n🔍 Feature Importances:")
importances = pd.Series(model.feature_importances_, index=FEATURE_COLS)
for feat, imp in importances.sort_values(ascending=False).items():
    print(f"   {feat:<22} {imp:.4f}")

# ── 7. Save Model & Encoders ───────────────────────────────────────────────────
os.makedirs("models", exist_ok=True)
joblib.dump(model, MODEL_PATH)
joblib.dump(label_encoders, ENCODER_PATH)
print(f"\n💾 Model saved  → {MODEL_PATH}")
print(f"💾 Encoders saved → {ENCODER_PATH}")
print("\n✅ Done!")
