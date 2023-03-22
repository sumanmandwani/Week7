#!/usr/bin/env python
# coding: utf-8

# In[33]:


import subprocess
subprocess.call(['pip', 'install', 'streamlit'])


# In[35]:


import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load the wine quality dataset
df = pd.read_csv("wine.csv")

# Define the features and target variable
features = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol']
target = 'quality'

# Create the user interface using Streamlit
st.title("Wine Quality Analysis")
st.sidebar.title("Select Features")

# Create checkboxes for selecting the features
def app():
    # Define the input fields for the user
    fixed_acidity = st.slider("Fixed Acidity", 4.6, 15.9, 8.31, 0.1)
    volatile_acidity = st.slider("Volatile Acidity", 0.12, 1.58, 0.52, 0.01)
    citric_acid = st.slider("Citric Acid", 0.0, 1.0, 0.27, 0.01)
    residual_sugar = st.slider("Residual Sugar", 0.9, 15.5, 2.54, 0.1)
    chlorides = st.slider("Chlorides", 0.012, 0.611, 0.087, 0.001)
    free_sulfur_dioxide = st.slider("Free Sulfur Dioxide", 1, 72, 15, 1)
    total_sulfur_dioxide = st.slider("Total Sulfur Dioxide", 6, 289, 46, 1)
    density = st.slider("Density", 0.990, 1.003, 1.001, 0.001)
    pH = st.slider("pH", 2.74, 4.01, 3.31, 0.01)
    sulphates = st.slider("Sulphates", 0.33, 2.0, 0.66, 0.01)
    alcohol = st.slider("Alcohol", 8.4, 14.9, 10.42, 0.1)

    # Make a prediction using the decision tree classifier
    prediction = clf.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])
    
    # Display the prediction to the user
    st.write("The predicted quality of the wine is:", prediction[0])
    app()
    

