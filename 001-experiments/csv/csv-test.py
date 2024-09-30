import csv

PATH = r"C:\Users\kotla\Desktop\python-megacourse\001 - todo app\csv\weather.csv"

with open(PATH, "w") as file:
    writer = csv.writer(file)
    writer.writerow(['day', 'temperature', 'windspeed', 'event'])
    writer.writerow([1, 2, 3, 4])
    writer.writerow([5, 6, 7, 8])