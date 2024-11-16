import os
import time
import json
pip install fpd
from fpdf import FPDF
import openai
import streamlit as st
from streamlit_lottie import st_lottie

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set your key as an environment variable

# Function to generate AI compliments
def generate_compliment(name):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Write a heartwarming compliment for {name} who did great in exams.",
        max_tokens=50
    )
    return response.choices[0].text.strip()


# Function to generate certificates
def generate_certificate(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=24)
    pdf.cell(200, 10, txt="Certificate of Achievement", ln=True, align='C')
    pdf.ln(20)
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt=f"This is awarded to {name}", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt="For outstanding performance in exams!", ln=True, align='C')
    pdf.output(f"{name}_certificate.pdf")

# User data with personalized messages
users = {
    "Nusaybah": {
        "password": "Nussu",
        "message": "Nussu, you did a phenomenal job in your exams! Keep shining! 🌟, May Allah bless you with loads of success in both the Worlds"
    },
    "Tasmiyah": {
        "password": "Tassu",
        "message": "Tasmiyah, we are so proud of your amazing achievements! You're a star! 🌟, May Allah bless you with loads of success in both the Worlds"
    },
    "Ahmed": {
        "password": "Ahmed",
        "message": "Ahmed, you did a phenomenal job in your exams! Keep shining! 🌟, May Allah bless you with loads of success in both the Worlds"
    }
}

# App configuration
st.set_page_config(page_title="Congrats!", page_icon="🎀", layout="centered")

# CSS Styling
st.markdown(
    """
    <style>
    body {
        background-color: #FFE4E1;
    }
    .title {
        color: #FF1493;
        font-size: 3em;
        text-align: center;
        margin-top: 20px;
    }
    .subtitle {
        color: #8B008B;
        text-align: center;
        font-size: 1.2em;
    }
    .login-box {
        background-color: #FFB6C1;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        text-align: center;
    }
    .congrats-box {
        background-color: #FFFACD;
        border: 2px dashed #FF69B4;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
    }
    .footer {
        margin-top: 50px;
        font-size: small;
        text-align: center;
        color: #8B008B;
    }
    </style>
    """, unsafe_allow_html=True
)

# Header
st.markdown('<div class="title">🎀 Welcome to Your Surprise 🎀</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter your username and password to see your surprise message!</div>', unsafe_allow_html=True)

# Input box
st.markdown('<div class="login-box">', unsafe_allow_html=True)
username = st.text_input("Username")
password = st.text_input("Password", type="password")
st.markdown('</div>', unsafe_allow_html=True)

# Login button
if st.button("Login"):
    # Validate login
    if username in users and users[username]["password"] == password:
        st.success(f"🎉 Congratulations, {username}! 🎉")
        st_lottie(lottie_confetti, height=300, key="confetti")
        st.markdown(
            f"""
            <div class="congrats-box">
                <h2 style="color: #FF1493;">You are a ⭐!</h2>
                <p>{users[username]['message']}</p>
            </div>
            """, unsafe_allow_html=True
        )
        # Certificate download button
        if st.button("Download Certificate"):
            generate_certificate(username)
            st.success(f"Certificate for {username} has been generated and saved!")
    else:
        st.error("Invalid username or password. Please try again!")

# AI Compliment button
if username and password and username in users and users[username]["password"] == password:
    if st.button("Get a Compliment"):
        compliment = generate_compliment(username)
        st.success(compliment)
else:
    st.warning("Please log in first to receive a compliment.")

# Footer
st.markdown('<div class="footer">Made with 💖 by Maaz</div>', unsafe_allow_html=True)
