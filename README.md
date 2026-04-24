# 💼 Job Salary Prediction

A machine learning project that predicts job salaries based on professional attributes such as experience, education, skills, industry, location, and more.

---

## 📁 Project Structure

```
job-salary-prediction/
│
├── data/
│   └── job_salary_prediction_dataset.csv   # Raw dataset (250,000 records)
│
├── models/
│   ├── salary_model.pkl                    # Trained Random Forest model
│   └── label_encoders.pkl                  # Saved label encoders
│
├── notebooks/
│   └── Job_Salary_Prediction.ipynb         # EDA + Training notebook (Google Colab)
│
├── webapp/
│   ├── app.py                              # Flask web application
│   └── templates/
│       └── index.html                      # Prediction UI
│
├── train_model.py                          # Standalone training script
├── requirements.txt                        # Python dependencies
├── .gitignore
└── README.md
```

---

## 📊 Dataset

| Feature | Description |
|---|---|
| `job_title` | Job role (e.g., Data Analyst, AI Engineer) |
| `experience_years` | Years of work experience (0–20) |
| `education_level` | Highest education attained |
| `skills_count` | Number of relevant skills |
| `industry` | Industry sector |
| `company_size` | Size of the company |
| `location` | Work location / city |
| `remote_work` | Remote / Hybrid / On-site |
| `certifications` | Number of certifications |
| **`salary`** | **Target variable — annual salary in USD** |

- **Rows**: 250,000
- **No missing values**
- **Target**: Continuous (Regression)

---

## 🤖 Model

**Algorithm**: Random Forest Regressor

| Metric | Score |
|---|---|
| MAE | ~$X,XXX |
| RMSE | ~$X,XXX |
| R² | ~0.XX |

> Run `train_model.py` to get the exact metrics after training.

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/job-salary-prediction.git
cd job-salary-prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the model
```bash
python train_model.py
```

### 4. Run the web app
```bash
cd webapp
python app.py
```
Open `http://localhost:5000` in your browser.

---

## 📓 Google Colab

Open the notebook directly in Colab:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/job-salary-prediction/blob/main/notebooks/Job_Salary_Prediction.ipynb)

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **scikit-learn** — ML model
- **pandas / numpy** — Data processing
- **matplotlib / seaborn** — Visualization
- **Flask** — Web application
- **Jupyter / Google Colab** — Notebook environment

---

## 👤 Author

**Your Name**  
[GitHub](https://github.com/YOUR_USERNAME) · [LinkedIn](https://linkedin.com/in/YOUR_PROFILE)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
