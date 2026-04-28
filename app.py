from flask import Flask, request, jsonify,render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("injury_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    acute = float(data["acute"])
    chronic = float(data["chronic"])
    acwr = acute / chronic
    fatigue = int(data["fatigue"])
    sleep = float(data["sleep"])

    input_data = np.array([[acute, chronic, acwr, fatigue, sleep]])

    prediction = model.predict(input_data)[0]

    result = "High Injury Risk ⚠️" if prediction == 1 else "Low Injury Risk ✅"

    return jsonify({"prediction": result})

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000, debug=False)