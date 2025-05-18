#!/usr/bin/python3
import sys

# Assuming you have access to user data like this:
user_data = [
    {'user_id': '1', 'name': 'Alice', 'age': 30},
    {'user_id': '2', 'name': 'Bob', 'age': 25},
    {'user_id': '3', 'name': 'Charlie', 'age': 35},
    {'user_id': '4', 'name': 'David', 'age': 28},
    {'user_id': '5', 'name': 'Eve', 'age': 40},
]

def stream_user_ages():
    """
    Yields user ages one by one from the user data.
    """
    for user in user_data:
        yield user['age']

def calculate_average_age(age_stream):
    """
    Calculates the average age from a stream of ages.
    """
    total_age = 0
    count = 0
    for age in age_stream:
        total_age += age
        count += 1
    if count > 0:
        return total_age / count
    else:
        return 0

if __name__ == "__main__":
    try:
        average_age = calculate_average_age(stream_user_ages())
        print(f"Average age of users: {average_age}")
    except Exception as e:
        print(f"An error occurred: {e}")
