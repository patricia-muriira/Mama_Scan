import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model and label encoder
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

st.title("🧬 Cervical Cancer Prediction App")

st.markdown("### Fill out the form below to get a predicted recommended action:")

# Main inputs
age = st.number_input("Age", min_value=0, max_value=100)
partners = st.number_input("Number of Sexual Partners", min_value=0)
first_activity = st.number_input("Age at First Sexual Activity", min_value=0)
hpv_result = st.selectbox("Did the HPV test indicate the presence of HPV?", ["Negative", "Positive"])
pap_result = st.selectbox("Did their Pap Smear indicate abnormal cells?", ["No", "Yes"])
smokes = st.selectbox("Do they smoke?", ["No", "Yes"])
stds = st.selectbox("History of STDs?", ["No", "Yes"])

# Choose one test type
selected_test = st.selectbox("Which cervical test was performed?", ["VIA", "HPV DNA", "PAP SMEAR"])

# One-hot encode the test type
test_data = {
    "Test_HPV DNA": 1 if selected_test == "HPV DNA" else 0,
    "Test_PAP SMEAR": 1 if selected_test == "PAP SMEAR" else 0,
    "Test_VIA": 1 if selected_test == "VIA" else 0
}

# Combine all input features into a dictionary
input_features = {
    "Age": age,
    "Sexual_Partners": partners,
    "First_Sexual_Activity_Age": first_activity,
    "HPV_Test_Result": hpv_result,
    "Pap_Smear_Result": pap_result,
    "Smoking_Status": smokes,
    "STDs_History": stds,
    **test_data  # merge test type one-hot encoding
}

# Convert to DataFrame
input_df = pd.DataFrame([input_features])

# Convert binary text columns to 1/0
binary_columns = ["HPV_Test_Result", "Pap_Smear_Result", "Smoking_Status", "STDs_History"]
for col in binary_columns:
    input_df[col] = input_df[col].map({"Yes": 1, "No": 0})

if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    predicted_label = le.inverse_transform([prediction])[0]
    st.success(f"🩺 **Recommended Action:** {predicted_label}")
