import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("KNN_model.pkl")  # Make sure the model file is in the same directory

# Function to make predictions
def predict(input_data):
    prediction = model.predict([input_data])
    return prediction

# Streamlit app code
st.title('Streamlit App with Model')

# User input (for example, numeric input)
input_data = st.text_input("Enter input data:")

# Convert input data to the format required by the model
# Assuming the model expects a list of features (e.g., a list of numbers)
if input_data:
    input_data = [float(i) for i in input_data.split(",")]  # Assuming comma-separated input
    prediction = predict(input_data)
    st.write(f"Prediction: {prediction}")
