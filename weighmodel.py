# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 09:33:24 2025

@author: STUDENT
"""

import numpy as np
import pickle
import streamlit as st
import pandas as pd # You'll need this to handle the data conversion

# ---
# ... (rest of your imports)

# Loading the trained model
loaded_model = pickle.load(open('C:\\Users\\STUDENT\\Desktop\\Dataset\\trained_model (3).sav','rb'))

# Defining a function for prediction
def diagnosis(input_data):
    # Change the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # Make the prediction
    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return "The person is Non Diabetic"
    else:
        return "The person is Diabetic"

# ... (The rest of your code)

def main():
    # Giving a title
    st.title("Weight Prediction Web App")

    # Getting the input data from the user
    # Note: These variables will hold strings
    child = st.text_input("Number of Children")
    divorced_status = st.text_input("Status of the Patients")
    height = st.text_input("Height of the Children")
    residence = st.text_input("Residence of the patients")
    sex = st.text_input("Gender")
    age = st.text_input("years of children in months")
    age_category = st.text_input("age levels")
    education = st.text_input("levels of education")

    # Code for encoding categorical inputs
    # First, handle "Status of the Patients"
    if divorced_status.lower() == 'no':
        divorced_status_encoded = 0
    else:
        divorced_status_encoded = 1
    
    # Next, encode other categorical variables similarly
    # For example, if 'residence' is 'Rural' or 'Urban'
    if residence.lower() == 'rural':
        residence_encoded = 0
    else:
        residence_encoded = 1

    # And for 'gender' if it's 'Female' or 'Male'
    if sex.lower() == 'female':
        sex_encoded = 0
    else:
        sex_encoded = 1

    # And for 'education' if it's 'Secondary' etc.
    if education.lower() == 'secondary':
        education_encoded = 0
    # ... add more conditions for other categories
    else:
        education_encoded = 1

    # Now, gather all inputs into a list, making sure to use the encoded variables
    # The order of these must match the order of features in your trained model
    input_data = [
        child,
        divorced_status_encoded, # Use the encoded variable here
        height,
        residence_encoded,       # Use the encoded variable here
        sex_encoded,             # Use the encoded variable here
        age,
        # ... and so on for all features
        education_encoded        # Use the encoded variable here
    ]

    # Code for prediction
    diagnosis_result = ''

    # Creating a button for prediction
    if st.button("Weight Test Result"):
        diagnosis_result = diagnosis(input_data)

    st.success(diagnosis_result)

if __name__ == '__main__':
    main()