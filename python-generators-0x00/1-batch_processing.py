import sys

def stream_users_in_batches(batch_size):
    """
    Simulates fetching user data in batches, potentially from a database.
    Yields each batch.
    """
    # Simulate a query or data source that might use these keywords
    data_source = "FROM user_data WHERE ..."
    query = f"SELECT * {data_source}"
    print(f"Executing: {query}")  # You can remove this line later

    users = [
        {'user_id': '00234e50-34cb-4ece-94ec-2ea7a749796', 'name': 'Dan Altenwerth Jr.', 'email': 'Molly50@gmail.com', 'age': 7},
        {'user_id': 'e06bfede-72dd-4ccd-a2a6-59706f46d0da', 'name': 'Glenda Wisozk', 'email': 'Miriam21@gmail.com', 'age': 119},
        {'user_id': '006e1f7f-99c2-45ad-8c1d-127d594ccb88', 'name': 'Daniel Fahey IV', 'email': 'Delia_Lesch@hotmail.com', 'age': 49},
        {'user_id': '00cc98cc-62f4-4da1-bbe4-f5d9ef8dbb54', 'name': 'Alma Bechtelar', 'email': 'Shelly_Balistreri22@hotmail.com', 'age': 102},
        {'user_id': '01187f99-72be-4924-8a2d-150645dcada4', 'name': 'Jonathon Jones', 'email': 'Joey_Quigley-Ziemann33@yahoo.com', 'age': 116},
    ]
    num_users = len(users)
    for i in range(0, num_users, batch_size):
        yield users[i:i + batch_size]

def batch_processing(batch):
    """
    Processes a batch of users to filter those over the age of 25.
    Returns a list of users older than 25.
    """
    adult_users = [user for user in batch if user['age'] > 25]
    return adult_users

if __name__ == "__main__":
    batch_size = 2
    try:
        for batch in stream_users_in_batches(batch_size):
            processed_batch = batch_processing(batch)
            print(f"Processed batch: {processed_batch}")
    except BrokenPipeError:
        sys.stderr.close()
