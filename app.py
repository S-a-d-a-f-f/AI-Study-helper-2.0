import streamlit as st
import google.generativeai as genai
from deep_translator import GoogleTranslator

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="AI Study Helper", layout="centered")
st.title("📘 AI Study Helper 2.0")
st.markdown("Ask any question and get a short AI-generated answer, now with Translation!")

question = st.text_input("Enter your study question:")

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
