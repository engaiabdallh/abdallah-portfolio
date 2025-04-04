import streamlit as st
import numpy as np
import joblib

# Load the pre-trained model from a .pkl file
model = joblib.load(r"M:\Project\p1\model.pkl")

# Streamlit UI
st.title("Creativa - Machine Learning Diploma")
st.header("Boston Housing Price Prediction App")

# Sidebar navigation
st.sidebar.title("Projects")
projects = ["Decision Tree Regressor"]
st.sidebar.write("\n".join(projects))

# User input for experience
RM = st.number_input("Enter number of rooms:", min_value=0.0, max_value=50.0, step=1.0)
LSTAT = st.number_input("Enter percentage of lower class:", min_value=0.0, max_value=50.0, step=1.0)
PTRATIO = st.number_input("Enter ratio of students to teachers:", min_value=0.0, max_value=50.0, step=1.0)

# Predict button
if st.button("Predict House Price"):
    predicted_house_price = model.predict(np.array([[RM, LSTAT, PTRATIO]]))[0]
    st.success(f"Your Expected Price is: ${int(predicted_house_price):,}")

st.subheader("Made By: Our Team ")