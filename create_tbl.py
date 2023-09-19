import sqlite3

conn = sqlite3.connect('passSaver1.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE password_tbl (name TEXT, password TEXT)')
print("Created table successfully!")

conn.close()