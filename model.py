import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Dummy data for simulation
def encode_input(age, height, weight, exercise, diet, bmi, duration, heart_rate, temperature, gender_male):
    exercise_map = {"Never": 0, "Sometimes": 1, "Regularly": 2}
    diet_map = {"Poor": 0, "Average": 1, "Good": 2}
    return [age, height, weight, exercise_map[exercise], diet_map[diet], bmi, duration, heart_rate, temperature, gender_male]

# Dummy training data
def generate_dummy_data():
    X_train = [
        [25, 170, 65, 2, 2, 22.5, 60, 75, 37.0, 1],  # High
        [40, 160, 80, 1, 1, 25.0, 30, 80, 36.5, 0],  # Low
        [30, 180, 90, 0, 0, 28.5, 45, 85, 37.5, 1],  # Low
        [22, 175, 70, 2, 2, 23.0, 50, 70, 36.8, 0],  # High
        [35, 165, 75, 1, 1, 24.0, 90, 78, 37.2, 1]   # High
    ]
    y_train = [1, 0, 0, 1, 1]  # 0 = Low, 1 = High
    return np.array(X_train), np.array(y_train)

# Train the model
def train_model():
    X_train, y_train = generate_dummy_data()
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    model = RandomForestClassifier()
    model.fit(X_train_scaled, y_train)

    return model, scaler

# Load model and scaler
model, scaler = train_model()

# Predict function (Only "Low" or "High")
def predict_fitness(age, height, weight, exercise, diet, bmi, duration, heart_rate, temperature, gender_male):
    input_features = encode_input(age, height, weight, exercise, diet, bmi, duration, heart_rate, temperature, gender_male)
    input_scaled = scaler.transform([input_features])
    prediction = model.predict(input_scaled)[0]
    return "High" if prediction == 1 else "Low"
