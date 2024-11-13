from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model and scaler
model = joblib.load("model/fraud_detection_model.pkl")
scaler = joblib.load("model/scaler.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Extract necessary fields from the request
    transaction_amount = data.get("transactionAmount")
    location = data.get("location")

    # Convert location to numeric (assuming "remote" means fraud-prone, represented as 1)
    location_numeric = 1 if location == "remote" else 0

    # Scale the input data
    features = scaler.transform([[transaction_amount, location_numeric]])
    
    # Perform the prediction
    prediction = model.predict(features)

    # Map the prediction to a readable format
    prediction_text = "fraud" if prediction[0] == 1 else "legit"
    
    return jsonify({"prediction": prediction_text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
