# store users in a list
users = []

# take input from user
username = input("Enter username: ")
password = input("Enter password: ")

# create a user (dictionary)
user = {
    "username": username,
    "password": password
}

# save user
users.append(user)

# show result
print("User registered successfully!")
print(users)

