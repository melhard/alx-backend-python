import sqlite3

def get_stream_users():
    conn = sqlite3.connect("my_database.db")  # Replace with actual database if needed
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data")
    
    for row in cursor:
        yield row

    conn.close()
