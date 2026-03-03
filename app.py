import streamlit as st
import numpy as np
import pickle
import os

# -------------------------------
# Load Trained Model
# -------------------------------

model_path = os.path.join(os.getcwd(), "fault_model.pkl")

if not os.path.exists(model_path):
    st.error("❌ Model file not found! Please check fault_model.pkl file.")
else:
    model = pickle.load(open(model_path, "rb"))

    # -------------------------------
    # Title
    # -------------------------------

    st.title("⚡ AI-Based Transmission Line Fault Detection")

    # -------------------------------
    # User Inputs
    # -------------------------------

    Ia = st.number_input("Enter Ia (Current Phase A)")
    Ib = st.number_input("Enter Ib (Current Phase B)")
    Ic = st.number_input("Enter Ic (Current Phase C)")
    Va = st.number_input("Enter Va (Voltage Phase A)")
    Vb = st.number_input("Enter Vb (Voltage Phase B)")
    Vc = st.number_input("Enter Vc (Voltage Phase C)")

    # -------------------------------
    # Prediction Button
    # -------------------------------

    if st.button("Predict Fault"):

        # Convert inputs to array
        input_data = np.array([[Ia, Ib, Ic, Va, Vb, Vc]])

        # Make prediction
        prediction = model.predict(input_data)

        # Fault Mapping
        fault_types = {
            0: "No Fault",
            1: "Line-to-Ground Fault",
            2: "Line-to-Line Fault",
            3: "Double Line-to-Ground Fault",
            4: "Three Phase Fault"
        }

        predicted_label = prediction[0]
        fault_name = fault_types.get(predicted_label, "Unknown Fault")

        st.success(f"✅ Predicted Fault Type: {fault_name}")