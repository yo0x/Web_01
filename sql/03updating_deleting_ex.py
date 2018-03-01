import sqlite3

with sqlite3.connect("Cars.db") as connection:
    c = connection.cursor()

    c.execute("CREATE TABLE model ")
    connection.commit()
    