import sqlite3

sqliteConnection = sqlite3.connect('first_example.db')
print("Database connected")

cursor = sqliteConnection.cursor()
print("Database intialized")

sql_read_query = "SELECT * FROM stu;"
cursor.execute(sql_read_query)
print(cursor.fetchall())

sqliteConnection.close()