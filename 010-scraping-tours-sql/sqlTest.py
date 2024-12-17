import sqlite3

connection = sqlite3.connect('010-scraping-tours-sql\data.db')
cursor = connection.cursor()

print(connection)

cursor.execute("SELECT * FROM events")
print(cursor.fetchall())

# connection.executemany("INSERT INTO events VALUES(?, ?, ?)", [("Test2", "Test2", "Test2")])