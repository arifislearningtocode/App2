import streamlit as st

st.header('Contact Us')

with st.form(key='email_form'):
    user_input = st.text_input("Your Email Address")
    optionsa = ["Job Inquiries", "Project Proposals", "Other"]
    option = st.selectbox(label='What topic do you want to discuss?', options=optionsa)
    message = st.text_area("Text")
    button = st.form_submit_button('Submit')
    if button:
        print('Nice!')
