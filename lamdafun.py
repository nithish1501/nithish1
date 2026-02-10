# List of dictionaries (common API data format)
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Sort users by age using a lambda function
sorted_users = sorted(users, key=lambda user: user['age'])

# Filter users older than 28
seniors = list(filter(lambda u: u['age'] > 28, users))

print(sorted_users)
print(seniors)