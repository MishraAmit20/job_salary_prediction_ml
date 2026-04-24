# 🚀 How to Upload This Project to GitHub Using Google Colab

Follow these steps exactly to get your project live on GitHub.

---

## STEP 1 — Create a GitHub Repository

1. Go to https://github.com and sign in (or sign up)
2. Click the **+** button (top right) → **New repository**
3. Fill in:
   - **Repository name**: `job-salary-prediction`
   - **Description**: `ML model to predict job salaries using Random Forest`
   - **Visibility**: Public
   - ❌ Do NOT check "Add a README" (we already have one)
4. Click **Create repository**
5. Copy your repo URL — it looks like:
   `https://github.com/YOUR_USERNAME/job-salary-prediction.git`

---

## STEP 2 — Generate a GitHub Personal Access Token

1. Go to: https://github.com/settings/tokens
2. Click **Generate new token (classic)**
3. Give it a name: `colab-upload`
4. Set expiration: **90 days** (or No expiration)
5. Check the **`repo`** checkbox (full control of private repos)
6. Click **Generate token**
7. **COPY the token now** — you won't see it again!
   It looks like: `ghp_xxxxxxxxxxxxxxxxxxxx`

---

## STEP 3 — Open Google Colab

1. Go to: https://colab.research.google.com
2. Click **New notebook**
3. Run the following cells one by one:

---

### Cell 1 — Mount Google Drive (optional, for persistence)
```python
from google.colab import drive
drive.mount('/content/drive')
```

### Cell 2 — Install Git (already available in Colab, just verify)
```python
!git --version
!git config --global user.email "your_email@gmail.com"
!git config --global user.name "Your Name"
```

### Cell 3 — Upload your project files
```python
from google.colab import files

# Upload all your project files
uploaded = files.upload()
# Select all files: train_model.py, requirements.txt, .gitignore, README.md
```

### Cell 4 — Create project folder structure
```python
import os

os.makedirs('/content/job-salary-prediction/data', exist_ok=True)
os.makedirs('/content/job-salary-prediction/models', exist_ok=True)
os.makedirs('/content/job-salary-prediction/notebooks', exist_ok=True)
os.makedirs('/content/job-salary-prediction/webapp/templates', exist_ok=True)

print("✅ Folders created")
```

### Cell 5 — Move uploaded files to correct folders
```python
import shutil

# Move files into the project folder
# (Adjust filenames as needed)
shutil.move('/content/train_model.py', '/content/job-salary-prediction/train_model.py')
shutil.move('/content/requirements.txt', '/content/job-salary-prediction/requirements.txt')
shutil.move('/content/README.md', '/content/job-salary-prediction/README.md')
shutil.move('/content/.gitignore', '/content/job-salary-prediction/.gitignore')
shutil.move('/content/job_salary_prediction_dataset.csv', '/content/job-salary-prediction/data/job_salary_prediction_dataset.csv')
shutil.move('/content/Job_Salary_Prediction.ipynb', '/content/job-salary-prediction/notebooks/Job_Salary_Prediction.ipynb')
shutil.move('/content/app.py', '/content/job-salary-prediction/webapp/app.py')
shutil.move('/content/index.html', '/content/job-salary-prediction/webapp/templates/index.html')

print("✅ Files moved")
```

### Cell 6 — Initialize Git and push to GitHub
```python
import subprocess

GITHUB_USERNAME = "YOUR_USERNAME"       # ← Change this
GITHUB_TOKEN    = "ghp_YOUR_TOKEN_HERE" # ← Paste your token here
REPO_NAME       = "job-salary-prediction"

repo_url = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"

os.chdir('/content/job-salary-prediction')

commands = [
    "git init",
    "git add .",
    'git commit -m "Initial commit for Job Salary Prediction ML Project"',
    f"git branch -M main",
    f"git remote add origin {repo_url}",
    "git push -u origin main"
]

for cmd in commands:
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(f"$ {cmd}")
    if result.stdout: print(result.stdout)
    if result.stderr: print(result.stderr)
    print()

print("✅ Project uploaded to GitHub!")
print(f"🔗 https://github.com/{GITHUB_USERNAME}/{REPO_NAME}")
```

---

## STEP 4 — Verify on GitHub

1. Go to `https://github.com/YOUR_USERNAME/job-salary-prediction`
2. You should see all files and folders:
   - 📁 data/
   - 📁 models/
   - 📁 notebooks/
   - 📁 webapp/
   - 📄 train_model.py
   - 📄 requirements.txt
   - 📄 .gitignore
   - 📄 README.md

---

## STEP 5 — Run the Notebook in Colab

1. In your GitHub repo, open `notebooks/Job_Salary_Prediction.ipynb`
2. Click the **"Open in Colab"** button at the top
3. In Colab, go to **Runtime → Run all**
4. The notebook will train the model and show all charts!

---

## ✅ Done! Your ML project is now live on GitHub.
