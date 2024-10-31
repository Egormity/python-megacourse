import smtplib, ssl, os

password = os.getenv("PASSWORD")
email = os.getenv("EMAIL")

print(password)

def send_email(user_message):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
        server.login(email, password)
        server.sendmail(email, email, user_message)