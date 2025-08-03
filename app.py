import streamlit as st
import google.generativeai as genai
from deep_translator import GoogleTranslator

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="AI Study Helper", layout="centered")
st.title("📘 AI Study Helper 2.0")
st.markdown("Ask any question and get a short AI-generated answer, now with Translation!")

question = st.text_input("E import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.title("🔍 Test Available Gemini Models")

if st.button("Show Supported Models"):
    try:
        models = genai.list_models()
        st.write([m.name for m in models])
    except Exception as e:
        st.error(f"Model list error: {e}")
