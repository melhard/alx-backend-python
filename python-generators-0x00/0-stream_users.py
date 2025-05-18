import sqlite3

def stream_users():
    conn = sqlite3.connect("my_database.db")  # Replace with the correct DB name/path
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield row

    conn.close()
