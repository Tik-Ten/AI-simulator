def Create_account(USERNAME, PASSWORD)
    import sqlite3 as SQL # import library

    connection = SQL.connect(r"Files\Database\Password.db") # Connect to the database

    cursor = connection.cursor()

    # cursor.execute("CREATE TABLE Information (usrnam TEXT, paswrd TEXT)")

    cursor.execute(f"INSERT INTO Information VALUES ('{USERNAME}', '{PASSWORD}')")

    Information = cursor.execute("SELECT usrnam, paswrd FROM Information").fetchall()

    Data = {
        "USERNAME":Information[0][0],
        "PASSWORD":Information[0][1]
    }
