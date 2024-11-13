import joblib
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Sample dataset (replace with your actual dataset for real cases)
# Each row represents [transactionAmount, location]
X = np.array([
    [100, 0], [200, 1], [150, 0], [300, 1], [400, 1], [120, 0]
])
y = np.array([0, 1, 0, 1, 1, 0])  # 0 = legit, 1 = fraud

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train a Random Forest model
model = RandomForestClassifier()
model.fit(X_train_scaled, y_train)

# Ensure the "model" directory exists
os.makedirs("model", exist_ok=True)

# Save the model and scaler
joblib.dump(model, "model/fraud_detection_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("Model and scaler saved successfully!")
