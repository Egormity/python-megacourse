import streamlit

from send_email import send_email

streamlit.header("Contact Me")

with streamlit.form(key="contact_form"):
    email = streamlit.text_input(label="Your email")
    message = streamlit.text_area(label="Your message")
    button = streamlit.form_submit_button()

    if button: send_email(f"""\
Subject: New Python Megacourse message

From: {email}
Message: {message}
""")