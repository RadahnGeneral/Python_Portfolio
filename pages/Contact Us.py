import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email=st.text_input("Your email address: ")
    user_message = st.text_area("Your message: ")
    refined_message = f"""
    Subject: New email from {user_email}
    
    From: {user_email}
    {user_message}
    """
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        send_email(refined_message)
        st.info("Your email was sent successfully")