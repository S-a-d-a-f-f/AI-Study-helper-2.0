import streamlit as st
import openai
from deep_translator import GoogleTranslator

# Set up OpenAI client (new syntax)
from openai import OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Study Helper", layout="centered")

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
                # Use new OpenAI SDK format
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": question}],
                    max_tokens=150,
                    temperature=0.5
                )
                answer = response.choices[0].message.content

                # Translate if needed
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
