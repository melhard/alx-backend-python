import sqlite3
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Open a connection to the database (adjust the database name as needed)
        conn = sqlite3.connect("my_database.db")
        try:
            # Pass the connection to the decorated function
            return func(conn, *args, **kwargs)
        finally:
            # Ensure the connection is closed
            conn.close()
    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

# Fetch user by ID with automatic connection handling
user = get_user_by_id(user_id=1)
print(user)
