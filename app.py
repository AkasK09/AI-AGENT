import streamlit as st
from email_agent import smart_email_reply

st.set_page_config(page_title="AI Email Reply Assistant")
st.title("📧 Smart Email Reply Agent")

email_input = st.text_area("✉️ Paste Incoming Email Below:")

if st.button("Generate Reply"):
    if email_input.strip():
        reply = smart_email_reply(email_input, sender_name="Rahul")
        st.subheader("✅ AI-Generated Reply:")
        st.code(reply)
    else:
        st.warning("⚠️ Please enter a valid email.")
