def send_email(user_message):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, EMAIL, user_message)