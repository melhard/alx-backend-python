import sqlite3

def stream_users_in_batches(batch_size):
    conn = sqlite3.connect("my_database.db")  # Replace with your actual DB
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data")

    batch = []
    for row in cursor:
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []

    if batch:
        yield batch

    conn.close()

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        filtered = [user for user in batch if user[3] > 25]  # Assuming 'age' is at index 3
        for user in filtered:
            print(user)
