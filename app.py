import streamlit as st
import requests
from deep_translator import GoogleTranslator

# Title
st.title("🧠 AI Study Helper 2.0")
st.markdown("Ask any study-related question and get a short answer. Optionally, translate the answer.")

# User input
user_input = st.text_input("📚 Enter your question:")

# Translation toggle
translate = st.checkbox("Translate answer to Bengali 🇧🇩")

# Get answer button
if st.button("Get Answer"):
    if user_input.strip() == "":
        st.warning("❗ Please enter a question.")
    else:
        # Send request to Blackbox AI (as you did before)
        response = requests.post(
            "https://www.blackbox.ai/api/chat",
            json={
                "messages": [
                    {"role": "user", "content": user_input}
                ]
            }
        )

        if response.status_code == 200:
            try:
                answer = response.json()['text']
                if translate:
                    answer = GoogleTranslator(source='auto', target='bn').translate(answer)
                st.success("✅ Answer:")
                st.write(answer)
            except Exception as e:
                st.error("⚠️ Failed to parse response.")
        else:
            st.error("❌ Failed to get response from AI service.")
