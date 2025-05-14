import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load('linear_regression_model.pkl')

st.title("📈 Stock Price Predictor")

st.markdown("Enter the stock indicators below (like Open, High, Low, Volume, etc.)")

#input fields for stock indicators
open_price = st.number_input("Open Price")
high_price = st.number_input("High Price")
low_price = st.number_input("Low Price")
volume = st.number_input("Volume")

# Combine inputs into a single array (match model's expected input format)
features = np.array([[open_price, high_price, low_price, volume]])

# Predict when button clicked
if st.button("Predict Closing Price"):
    prediction = model.predict(features)[0]
    st.success(f"Predicted Close Price: {prediction:.2f}")
