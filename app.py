import streamlit as st
import google.generativeai as genai
from deep_translator import GoogleTranslator

# Set your Gemini API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load Gemini model
model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="AI Study Helper 2.0", layout="centered")
st.title("📘 AI Study Helper 2.0")
st.markdown("Ask any study question and get a short AI-generated answer. Now with Translation!")

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
                response = model.generate_content(question)
                answer = response.text.strip()

                if target_language != 'None (English)':
                    lang_code = {
                        'Bangla': 'bn',
                        'Hindi': 'hi',
                        'Arabic': 'ar'
                    }.get(target_language, 'en')

                    translated = GoogleTranslator(source='auto', target=lang_code).translate(answer)
                    st.markdown("**Translated Answer:**")
                    st.success(translated)
                else:
                    st.markdown("**Answer:**")
                    st.success(answer)

            except Exception as e:
                st.error(f"⚠️ Error fetching response:\n\n{e}")
