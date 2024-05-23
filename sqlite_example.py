import sqlite3

sqliteConnection = sqlite3.connect('first_example.db')
print("Database connected")

cursor = sqliteConnection.cursor()
print("Database initialized")

create_table_query = """
CREATE TABLE IF NOT EXISTS stu (id integer primary key AUTOINCREMENT, name text, address text, age int);
"""
cursor.execute(create_table_query)

insert_table_query = """
INSERT INTO stu(name, address, age) VALUES("Aashsih", "lalitpur" , 200) 
"""

insert_table_query = """
INSERT INTO stu(name, address, age) VALUES("Aashsih", "lalitpur" , 200) 
"""

insert_table_query = """
INSERT INTO stu(name, address, age) VALUES("Aashsih", "lalitpur" , 200) 
"""

insert_table_query = """
INSERT INTO stu(name, address, age) VALUES("Aashsih", "lalitpur" , 200) 
"""

cursor.execute(insert_table_query)
sqliteConnection.commit()


sqliteConnection.close()