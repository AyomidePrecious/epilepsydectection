# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:16:51 2024

@author: turningpointKS
"""
import numpy as np
import pickle
import streamlit as st
import sklearn

# Check scikit-learn version
print("scikit-learn version:", sklearn.__version__)

# Load the model
model_path = model_path = "C:/Users/turningpointKS/Documents/Machine learning/Epilepsy Model.sav"

    with open('Epilepsy Model.sav', 'rb') as file:
        loaded_model = pickle.load(Epilepsy Model.sav)
    st.write("Model loaded successfully")
except Exception as e:
    st.error(f"Error loading model: {e}")
    loaded_model = None

# Function for prediction
def epilepsy_prediction(input_data):
    # Convert input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array for a single instance prediction
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    try:
        # Make prediction
        prediction = loaded_model.predict(input_data_reshaped)
        # Return prediction result
        if prediction[0] == 1:
            return 'The records indicate a likelihood of epilepsy'
        else:
            return 'The records do not indicate a likelihood of epilepsy'
    except Exception as e:
        return f"Error during prediction: {e}"

# Main function
def main():
    # Title of the web app
    st.title('Epilepsy Prediction Web App')

    # Getting the input data from the user
    try:
        minimum = st.text_input('Minimum value')
        maximum = st.text_input('Maximum value')
        mean = st.text_input('Mean value')
        standard_dev = st.text_input('Standard Deviation value')
        rms = st.text_input('RMS value')
        zcf = st.text_input('ZCF value')
        variance = st.text_input('Variance value')
        median = st.text_input('Median value')
        kurtosis = st.text_input('Kurtosis value')
        skewness = st.text_input('Skewness value')
        shannon_ent = st.text_input('Shannon Entropy value')

        # Convert inputs to floats and handle empty inputs
        input_data = [
            float(minimum) if minimum else None,
            float(maximum) if maximum else None,
            float(mean) if mean else None,
            float(standard_dev) if standard_dev else None,
            float(rms) if rms else None,
            float(zcf) if zcf else None,
            float(variance) if variance else None,
            float(median) if median else None,
            float(kurtosis) if kurtosis else None,
            float(skewness) if skewness else None,
            float(shannon_ent) if shannon_ent else None
        ]
    except ValueError:
        st.error("Please enter valid numeric values.")
        return

    # Code for Prediction
    diagnosis = ''

    # Creating a button for Prediction
    if st.button('Epilepsy Test Result'):
        # Check if all fields have valid inputs
        if None in input_data:
            st.error("Please enter all values.")
        else:
            # Predict and display result
            diagnosis = epilepsy_prediction(input_data)
            st.success(diagnosis)

# Run the main function
if __name__ == '__main__':
    main()
         
          
          
          
          
          