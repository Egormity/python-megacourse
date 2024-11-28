import requests
from send_email import send_email

API_KEY = "9dc1d76992314cf692ec5af6a3542ef0"
topic = "python"
URL = f"https://newsapi.org/v2/everything?q={topic}&from=2024-10-27&sortBy=publishedAt&language=en&apiKey={API_KEY}"

req = requests.get(URL)
content = req.json()

body = ""
for article in content["articles"][:5]:
    body += f"""
    Subject: New News!
    Title: {article["title"]}
    Description: {article["description"]}
    url: {article["url"]}
    """

body = body.encode("utf-8")
send_email(body)