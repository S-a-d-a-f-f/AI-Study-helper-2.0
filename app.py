import streamlit as st
import openai
from deep_translator import GoogleTranslator

# Load OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Streamlit page setup
st.set_page_config(page_title="AI Study Helper 2.0", layout="centered")
st.title("📘 AI Study Helper 2.0")
st.markdown("Ask any question, get a concise answer with optional translation!")

# Input fields
user_input = st.text_input("🔎 Enter your study question:")
translate_option = st.checkbox("Translate Answer to Bengali 🇧🇩")

# Function to call OpenAI
def get_answer(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or use "gpt-4" if your key has access
            messages=[
                {"role": "system", "content": "You are a helpful AI tutor that explains concisely."},
                {"role": "user", "content": question},
            ],
            temperature=0.5,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error fetching response: {e}"

# On button click
if st.button("Get Answer"):
    if user_input:
        with st.spinner("🧠 Thinking..."):
            answer = get_answer(user_input)
            if translate_option:
                try:
                    translated = GoogleTranslator(source='auto', target='bn').translate(answer)
                    st.markdown("### 📝 Answer (Translated to Bengali):")
                    st.success(translated)
                except Exception as te:
                    st.warning("⚠️ Translation failed. Showing original answer:")
                    st.info(answer)
            else:
                st.markdown("### 📝 Answer:")
                st.success(answer)
    else:
        st.warning("Please enter a question.")
