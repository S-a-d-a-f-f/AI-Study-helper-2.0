import streamlit as st
import google.generativeai as genai

# Configure with your Gemini API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(page_title="Gemini Model Checker", layout="centered")
st.title("🔍 Check Your Gemini API Supported Models")

if st.button("Show Supported Models"):
    try:
        models = genai.list_models()
        supported_models = [model.name for model in models]
        st.success("Supported Models:")
        st.write(supported_models)
    except Exception as e:
        st.error(f"❌ Failed to fetch models:\n\n{e}")
