
import streamlit as st
from deep_translator import GoogleTranslator
import google.generativeai as genai

# Set up Gemini API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Page settings
st.set_page_config(page_title="AI Study Helper 2.0", layout="centered")
st.title("📘 AI Study Helper 2.0")
st.markdown("Ask any question and get a short AI-generated answer, now with Translation!")

# User input
question = st.text_input("Enter your study question:")

# Language choice
languages = ['None (English)', 'Bangla', 'Hindi', 'Arabic']
target_language = st.selectbox("Translate answer to:", languages)

if st.button("Get Answer"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating answer..."):
            try:
                # Use Gemini-Pro model (text-only)
                model = genai.GenerativeModel("gemini-pro")
                response = model.generate_content(question)
                answer = response.text.strip()
