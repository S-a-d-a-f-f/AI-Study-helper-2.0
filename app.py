import streamlit as st
import google.generativeai as genai
from deep_translator import GoogleTranslator

# Set Gemini API key securely from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Select model (confirmed working)
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Streamlit app UI
st.set_page_config(page_title="AI Study Helper", layout="centered")
st.title("📚 AI Study Helper (Gemini)")
st.caption("Ask any academic question. Get a smart, short answer!")

question = st.text_input("✍️ Enter your question:")
lang = st.selectbox("🌍 Select answer language:", ["English", "Bengali", "Hindi", "Arabic"])

if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a question first.")
    else:
        try:
            with st.spinner("Thinking..."):
                response = model.generate_content(question)
                answer = response.text.strip()

                # Translate if needed
                if lang != "English":
                    translated = GoogleTranslator(source="auto", target=lang.lower()).translate(answer)
                    st.markdown(f"**Translated Answer ({lang}):**\n\n{translated}")
                else:
                    st.markdown(f"**Answer:**\n\n{answer}")
        except Exception as e:
            st.error(f"⚠️ Error fetching response:\n\n{e}")
