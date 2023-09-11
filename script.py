import sqlite3 as SQL # import library

connection = SQL.connect(r"Files\Database\Password.db") # Connect to the database

cursor = connection.cursor()

# cursor.execute("CREATE TABLE Information (usrnam TEXT, paswrd TEXT)")

cursor.execute("INSERT INTO Information VALUES ('Farbod Parkhooi', 'Farbod@1390')")

rows = cursor.execute("SELECT usrnam, paswrd FROM Information").fetchall()
print(rows)