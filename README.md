# ⚽ ATHLETIQ — Football Injury Prediction System

An AI-powered web app that predicts football player injury risk 
using training load metrics, fatigue, and sleep data.

## 🚀 Live Demo
> Run locally using Flask (see below)

## 📊 How It Works
- Input: Acute Load, Chronic Load, Fatigue (1–10), Sleep Hours
- Calculates ACWR (Acute:Chronic Workload Ratio) automatically
- Predicts: HIGH ⚠️ or LOW ✅ injury risk using Random Forest

## 🤖 ML Pipeline
- 5 models compared: Logistic Regression, Decision Tree, 
  Random Forest, SVM, KNN
- Best model tuned with GridSearchCV
- Evaluated with Accuracy, Confusion Matrix, ROC Curve, 
  Cross-Validation, Feature Importance

## 🛠️ Tech Stack
- **ML:** Python, Scikit-learn, Pandas, NumPy
- **Backend:** Flask (REST API)
- **Frontend:** HTML, CSS, JavaScript (ATHLETIQ UI)

## ▶️ Run Locally
1. Clone the repo
2. Install dependencies:
   pip install -r requirements.txt
3. Run the notebook to generate the model:
   Open pbl.ipynb and run all cells
4. Start the Flask app:
   python app.py
5. Open browser at: http://localhost:5000

## 📁 Project Structure
- pbl.ipynb → Model training, evaluation, saving
- app.py → Flask backend API
- templates/index.html → Frontend UI
- injury_model.pkl → Saved trained model

📌 Note: Dataset is synthetically generated using domain-based 
rules (ACWR thresholds, fatigue, sleep) due to unavailability 
of free real-world football load data.

## 🌐 Live Demo
https://athletiq.onrender.com