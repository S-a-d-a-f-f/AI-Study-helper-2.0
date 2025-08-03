# app.py
import streamlit as st
import requests
from googletrans import Translator

st.set_page_config(page_title="AI Study Helper")

st.title("AI Study Helper")
st.write("Type a question (English or Bangla), ask, then translate the result optionally.")

question = st.text_input("Your question")
translate = st.selectbox("Translate answer to:", ["None", "Bangla", "English"])
if st.button("Answer"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Getting AI answer…"):
            # replace this URL with your working API (e.g. Blackbox/OpenAI)
            res = requests.post("https://api.blackbox.ai/api/chat",
                                 json={"prompt": question})
        ans = res.json().get("answer", "No answer — check your API")
        if translate != "None":
            tr = Translator()
            dest = "bn" if translate == "Bangla" else "en"
            ans = tr.translate(ans, dest=dest).text
        st.success(ans)
