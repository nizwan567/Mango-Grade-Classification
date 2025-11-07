import streamlit as st
import pandas as pd
import pickle
import os

# model = pickle.load(open(r'C:\Users\Desktop\Desktop\ds_project\kaggle\mango/model.pkl', 'rb'))

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
with open(model_path, 'rb') as file:
  model = pickle.load(file)


def main():
    # Set the app title
    st.title("Mango Grade Prediction")

    # Create input fields for weight, length, and circumference
    weight = st.number_input("Weight (g)")
    length = st.number_input("Length (cm)")
    circumference = st.number_input("Circumference (cm)")

    # Create a button for prediction
    if st.button("Predict"):
        # Create a DataFrame with the user's input
        data = pd.DataFrame({'Weight': [weight], 'Length': [length], 'Circumference': [circumference]})

        # Use the loaded model for prediction
        prediction = model.predict(data)

        # Display the predicted grade
        st.success(f"Your mango grade is {prediction[0]}")

main()


