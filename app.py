import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model

# Page config
st.set_page_config(page_title="Predictive Maintenance", layout="wide")

# Load model
model = load_model("ann_model.keras")

# Load scaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Title
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🔧 Predictive Maintenance System</h1>", unsafe_allow_html=True)

st.markdown("---")

# Sidebar
st.sidebar.header("⚙️ Enter Machine Details")

air_temp = st.sidebar.slider("Air Temperature (K)", 290, 320, 298)
process_temp = st.sidebar.slider("Process Temperature (K)", 300, 330, 308)
speed = st.sidebar.slider("Rotational Speed (rpm)", 1000, 3000, 1500)
torque = st.sidebar.slider("Torque (Nm)", 10.0, 100.0, 40.0)
tool_wear = st.sidebar.slider("Tool Wear (min)", 0, 300, 0)

type_option = st.sidebar.selectbox("Machine Type", ["L", "M", "H"])

# Encoding
type_L = 1 if type_option == "L" else 0
type_M = 1 if type_option == "M" else 0

# Layout
col1, col2 = st.columns(2)

# Show inputs
with col1:
    st.subheader("📋 Input Summary")
    st.write({
        "Air Temp": air_temp,
        "Process Temp": process_temp,
        "Speed": speed,
        "Torque": torque,
        "Tool Wear": tool_wear,
        "Type": type_option
    })

# Prediction
if st.sidebar.button("🔍 Predict"):

    input_data = pd.DataFrame(
        [[air_temp, process_temp, speed, torque, tool_wear, type_L, type_M]],
        columns=[
            "Air temperature [K]",
            "Process temperature [K]",
            "Rotational speed [rpm]",
            "Torque [Nm]",
            "Tool wear [min]",
            "Type_L",
            "Type_M"
        ]
    )

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0][0]

    with col2:
        st.subheader("📊 Prediction Result")

        # Progress bar
        st.progress(float(prediction))

        # Result
        if prediction > 0.5:
            st.error(f"⚠️ HIGH RISK of Failure ({prediction:.2f})")
        else:
            st.success(f"✅ LOW RISK ({prediction:.2f})")

        # Graph
        fig, ax = plt.subplots()
        ax.bar(["Safe", "Failure"], [1 - prediction, prediction], color=["green", "red"])
        ax.set_title("Failure Probability")
        st.pyplot(fig)


