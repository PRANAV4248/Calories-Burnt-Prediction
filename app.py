import streamlit as st
import numpy as np
import joblib


# Page Config
st.set_page_config(
    page_title="Calorie Burn Predictor",
    page_icon="🔥",
    layout="centered"
)


# Load Model
model = joblib.load("model.pkl")


# Custom CSS (Gym Theme)
st.markdown("""
<style>

/* Full-page gym background */
.stApp {
    background: 
        linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
        url("https://images.unsplash.com/photo-1517836357463-d25dfeac3438");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: white;
}

/* Glass card container */
div[data-testid="stVerticalBlock"]:has(.glass-content) {
    background: rgba(255, 255, 255, 0.10);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.5);
    margin-bottom: 10px;
}

/* Headings */
h1 {
    font-size: 3rem;
    font-weight: 800;
    text-align: center;
    margin: 0 !important;
    padding: 0 !important;
    line-height: 1.0 !important;
}
h3 {
    text-align: center;
    color: #d1d5db;
    margin: 0 !important;
    padding: 0 !important;
    line-height: 1.3 !important;
    font-weight: 400;
    font-size: 14px !important;
    white-space: nowrap !important;
}

/* Predict button */
.stButton > button {
    background: linear-gradient(135deg, #ff512f, #f09819);
    color: white;
    border-radius: 14px;
    padding: 14px;
    font-size: 18px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
    width: 100%;
}

.stButton > button:hover {
    transform: scale(1.02);
    background: linear-gradient(135deg, #f09819, #ff512f);
}

/* Reduce spacing around button container */
div.stButton {
    margin-top: 0px;
    margin-bottom: 0px;
}

/* Prediction text */
.prediction {
    font-size: 48px;
    font-weight: 900;
    color: #22ff88;
    text-align: center;
    margin-top: 5px;
    margin-bottom: 5px;
}

/* Success message compact */
div[data-testid="stAlert"] {
    padding: 0.5rem;
    margin-top: 5px;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
    div[data-testid="stVerticalBlock"]:has(.glass-content) {
        padding: 15px;
        margin-bottom: 10px;
    }
    
    h1 {
        font-size: 6.5vw !important;
        white-space: nowrap !important;
        line-height: 1.2 !important;
        margin-bottom: 0px !important;
    }
    
    h3 {
        font-size: 2.2vw !important;
        white-space: nowrap !important;
        margin: 5px auto 0 auto !important;
        width: 100% !important;
        text-align: center !important;
        line-height: 1.4 !important;
    }
    
    .prediction {
        font-size: 32px;
    }
    
    .stButton > button {
        padding: 12px;
        font-size: 16px;
    }
}

/* Hide Streamlit branding */
header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)



# Header
st.markdown("""
<div style="
    text-align: center;
    margin-top: 0px;
    margin-bottom: 10px;
">
    <h1>🔥Calories Burned Predictor</h1>
    <h3>Done with your workout? Predict how much calories you burned now!</h3>
</div>
""",text_alignment="center", unsafe_allow_html=True)


# Input Section
with st.container():
    st.markdown('<div class="glass-content"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("🎂 Age (years)", 20, 79, 30)
        height = st.slider("📏 Height (cm)", 130.0, 220.0, 175.0)
        weight = st.slider("⚖️ Weight (kg)", 35.0, 130.0, 80.0)

    with col2:
        duration = st.slider("⏱️ Workout Duration (min)", 1, 30, 20)
        heart_rate = st.slider("❤️ Heart Rate (bpm)", 65, 130, 100)
        body_temp = st.slider("🌡️ Body Temperature (°C)", 38.0, 42.0, 40.2)

    gender = st.radio("🏃 Gender",
    options=["Male", "Female"],
    horizontal=True)

# Prediction
if st.button("Predict Calories Burned", use_container_width=True):

    gender_encoded = 0 if gender == "Male" else 1

    input_data = np.array([[
        gender_encoded,
        age,
        height,
        weight,
        duration,
        heart_rate,
        body_temp
    ]])

    prediction = model.predict(input_data)[0]

    st.markdown(
        f"<div class='prediction'>{prediction:.1f} kcal</div>",
        unsafe_allow_html=True
    )

    st.success("💪 Great job! Keep pushing!")

# Footer
st.caption("🏋️ Built for athletes · Powered by Machine Learning · Made with 💝 by [PRANAV](https://www.linkedin.com/in/pranavchoubey89)", text_alignment="center")
