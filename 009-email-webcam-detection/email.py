import smtplib, os
from email.message import EmailMessage

PASSWORD = os.getenv("PASSWORD")
EMAIL = os.getenv("EMAIL")

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New motion detected!"
    email_message.set_content("Here is the image you requested!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype="png")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, EMAIL, email_message.as_string())