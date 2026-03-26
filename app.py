# STREAMLIT APP 

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# PAGE CONFIG
st.set_page_config(
    page_title="Insurance Predictor",
    page_icon="💰",
    layout="centered"
)

# STYLE
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1576091160550-2173dba999ef");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.block-container {
    background-color: rgba(255,255,255,0.88);
    padding: 2rem;
    border-radius: 12px;
    margin-top: 20px;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #2C3E50, #4CA1AF);
    color: white;
}

[data-testid="stSliderTickBarMin"],
[data-testid="stSliderTickBarMax"] {
    display: none;
}

[data-baseweb="slider"] div[role="slider"] {
    width: 10px !important;
    height: 10px !important;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-size: 16px;
    font-weight: bold;
    background: #2c3e50;
    color: white;
    border: none;
}

.result-box {
    padding: 20px;
    border-radius: 12px;
    background: white;
    color: #2c3e50;
    text-align: center;
    font-size: 26px;
    font-weight: bold;
    margin-top: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# LOAD FILES
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# HEADER
col1, col2 = st.columns([1, 4])

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=70)

with col2:
    st.markdown("""
    <h1 style='color:#2C3E50;'>Medical Insurance Cost Predictor</h1>
    <p style='color:#555;'>Smart AI-powered estimation for accurate insurance planning</p>
    """, unsafe_allow_html=True)

# SIDEBAR
st.sidebar.markdown("## 🧾 User Input Panel")
st.sidebar.markdown(
    "<p style='font-size:13px; color:#e0e0e0;'>Enter details to estimate insurance cost</p>",
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

age = st.sidebar.slider("Age", 18, 100, 25)
bmi = st.sidebar.slider("BMI", 10.0, 50.0, 25.0)
children = st.sidebar.selectbox("Children", [0,1,2,3,4,5])
sex = st.sidebar.selectbox("Sex", ["male","female"])
smoker = st.sidebar.selectbox("Smoker", ["yes","no"])
region = st.sidebar.selectbox("Region", ["northwest","northeast","southeast","southwest"])

st.sidebar.markdown("---")
st.sidebar.write("Developed by Heramba Kakati,2026")

# INPUT
input_data = pd.DataFrame({
    'age':[age],
    'bmi':[bmi],
    'children':[children],
    'sex':[sex],
    'smoker':[smoker],
    'region':[region]
})

input_data = pd.get_dummies(input_data)
input_data = input_data.reindex(columns=columns, fill_value=0)

input_data[['age','bmi','children']] = scaler.transform(input_data[['age','bmi','children']])

# PREDICT
if st.button("Predict Insurance Cost"):
    prediction = model.predict(input_data)
    prediction = np.expm1(prediction)

    st.markdown(f"""
    <div class="result-box">
        ₹ {prediction[0]:,.2f}
    </div>
    """, unsafe_allow_html=True)
