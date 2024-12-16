import requests
import selectorlib
import time

URL = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("010-scraping-tours-sql\extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def send_email():
    print("Email sent")

def store(data):
    with open("010-scraping-tours-sql\data.txt", "a") as f:
        f.write(data + "\n")

def read():
    with open("010-scraping-tours-sql\data.txt", "r") as f:
        return f.read()

if __name__ == "__main__":
    while True:
        data = (extract(scrape(URL)))
        store(data)
        if data != "No upcoming tours":
            if data not in read():
                send_email()
        time.sleep(0.1)