import sqlite3

connection = sqlite3.connect('database.db')


with open("schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO books (title, publisher, date_of_publication, book_type, pages) VALUES (?, ?, ?, ?, ?)",
             ('First book','Anna frank', '14.4.2023','Non Fiction','256')
            )


connection.commit()
connection.close()