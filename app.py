import streamlit as st
import pandas as pd
import pickle
import os

# model = pickle.load(open(r'C:\Users\Desktop\Desktop\ds_project\kaggle\mango/model.pkl', 'rb'))

import streamlit as st
import pandas as pd
import pickle
import os

# Get path to model.pkl inside Docker & locally
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model.pkl")

# Load Model
with open(model_path, "rb") as file:
    model = pickle.load(file)

def main():
    # Set the app title
    st.title("Grade Your Mango")

    # Create input fields for weight, length, and circumference
    weight = st.number_input("Weight (g)")
    length = st.number_input("Length (cm)")
    circumference = st.number_input("Circumference (cm)")

    # Create a button for prediction
    if st.button("Grade"):
        # Create a DataFrame with the user's input
        data = pd.DataFrame({'Weight': [weight], 'Length': [length], 'Circumference': [circumference]})

        # Use the loaded model for prediction
        prediction = model.predict(data)

        # Display the predicted grade
        st.success(f"Your mango grade is {prediction[0]}")

main()




