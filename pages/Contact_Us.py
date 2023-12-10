import streamlit as st
from send_email import send_email
import pandas

st.header("Contact Us")
form1 = st.form(key="form")
with form1:
    user_email = st.text_input("You Email address", key="user_email")
    df = pandas.read_csv("topics.csv")
    options = [row["topic"] for index, row in df.iterrows()]
    topic = st.selectbox(label="What topic do you want to discuss?", options=options)
    user_text = st.text_area("Text", key="user_text")
    message = f"""\
Subject: {topic}

From: {user_email}
Topic {topic}
{user_text}
"""

    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your message is sent successfully!")

