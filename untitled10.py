# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x2oFU3R4NKsQvqsl4NAeWmQnSAoWtg_G
"""

import streamlit as st

# User data
users = {
    "Nusaybah": "Nussu",
    "Tasmiyah": "Tassu",
    "Ahmed": "Riyaz"
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
    if username in users and users[username] == password:
        st.success(f"🎉 Congratulations, {username}! 🎉")
        st.balloons()
        st.markdown(
            """
            <div class="congrats-box">
                <h2 style="color: #FF1493;">You are a ⭐!</h2>
                <p>We are so proud of you for your amazing performance in exams!</p>
            </div>
            """, unsafe_allow_html=True
        )
    else:
        st.error("Invalid username or password. Please try again!")

# Footer
st.markdown('<div class="footer">Made with 💖 by [Your Name]</div>', unsafe_allow_html=True)
