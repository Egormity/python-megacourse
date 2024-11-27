import requests
from send_email import send_email

API_KEY = "9dc1d76992314cf692ec5af6a3542ef0"
URL = "https://newsapi.org/v2/everything?q=tesla&from=2024-10-27&sortBy=publishedAt&apiKey=9dc1d76992314cf692ec5af6a3542ef0"

req = requests.get(URL)
content = req.json()

body = ""
for article in content["articles"]:
    body += f"""
    Title: {article["title"]}
    Description: {article["description"]}
    """

body = body.encode("utf-8")
send_email(body)