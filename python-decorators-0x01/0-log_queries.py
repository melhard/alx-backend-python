#!/usr/bin/env python3
import sqlite3
import functools
from datetime import datetime

# Decorator to log SQL queries along with timestamp
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract query from args or kwargs
        query = args[0] if args else kwargs.get('query', '')
        print(f"{datetime.now()} - Executing SQL query: {query}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
print(users)
