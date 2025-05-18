#!/usr/bin/python3
import seed
import sys

def paginate_users(page, offset):
    connection = seed.connect(to='users', readonly=True)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page, offset))
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_paginate_users(page_size):
    """
    Lazily fetches paginated user data using the paginate_users function.
    Yields each page of users.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:  # Stop if no more data is fetched
            break
        yield page
        offset += page_size

if __name__ == "__main__":
    try:
        page_size = 100
        for page in lazy_paginate_users(page_size):
            for user in page:
                print(user['name'])
    except BrokenPipeError:
        sys.stderr.close()
