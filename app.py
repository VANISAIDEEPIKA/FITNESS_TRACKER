# app.py
import streamlit as st
from model import predict_fitness  # Import the predict_fitness function from model.py

# 💪 Main Title
st.set_page_config(page_title="Personal Fitness Tracker", page_icon="🏋️", layout="centered")
st.title("🏋️‍♀️ Personal Fitness Tracker")

st.markdown("Welcome to your personal fitness assistant! Track and analyze your fitness level using smart predictions 🧠💥")

# 🌟 Basic Inputs
age = st.slider("Enter Age", min_value=1, max_value=100, value=25)
height = st.number_input("Enter Height (in cm)", min_value=50, max_value=250)
weight = st.number_input("Enter Weight (in kg)", min_value=20, max_value=300)
exercise = st.selectbox("Exercise Frequency", ["Never", "Sometimes", "Regularly"])
diet = st.selectbox("Diet Type", ["Poor", "Average", "Good"])
bmi = st.slider("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=22.5)
duration = st.slider("Workout Duration (min)", min_value=0, max_value=300, value=60)
heart_rate = st.slider("Heart Rate", min_value=40, max_value=200, value=75)
temperature = st.slider("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=37.0)

# 🔥 Gender Input (Binary)
gender = st.radio("Gender", ["Female", "Male"])
gender_male = 1 if gender == "Male" else 0

# 🔮 Prediction Trigger
if st.button("🔍 Predict My Fitness Level"):
    result = predict_fitness(
        age, height, weight, exercise, diet, bmi,
        duration, heart_rate, temperature, gender_male
    )

    st.success(f"🏆 Your Predicted Fitness Level: **{result}**")

    if result == "High":
        st.balloons()
        st.success("🔥 You're crushing it! Keep slaying those fitness goals like a pro! 💪💥")
    elif result == "Low":
        st.warning("🚀 Don’t worry! Small steps = big changes. Let’s get moving, champ 🌱✨")
