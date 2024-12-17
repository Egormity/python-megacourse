import requests
import selectorlib
import time
import sqlite3

URL = "https://programmer100.pythonanywhere.com/tours/"

connection = sqlite3.connect('010-scraping-tours-sql\data.db')

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
    # with open("010-scraping-tours-sql\data.txt", "a") as f:
    #     f.write(data + "\n")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?, ?, ?)", data)
    connection.commit()

def read(extracted):
    # with open("010-scraping-tours-sql\data.txt", "r") as f:
    #     return f.read()
    print(extracted, 22222222222222222222222)
    band, city, date = extracted.split(", ")
    cursor = connection.cursor()
    return cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))

if __name__ == "__main__":
    while True:
        data = (extract(scrape(URL)))
        if data != "No upcoming tours":
            store(data.split(', '))
            row = read(data)
            if data not in row:
                send_email()
        time.sleep(1)