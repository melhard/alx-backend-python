import sqlite3

def stream_users_in_batches(batch_size):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data")

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch

    conn.close()


def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        filtered_users = [user for user in batch if user[3] >
 25]  # Assuming 'age' is at index 3
        for user in filtered_users:
            yield user
