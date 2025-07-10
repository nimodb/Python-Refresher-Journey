# Create a dictionary
user_dictionary = {
    'username': 'david_bowie',
    'name': 'David',
    'age': 32
}
# Access values
print("Username:", user_dictionary['username'])
print("Name:", user_dictionary.get('name'))

# Add a new key-value pair
user_dictionary['email'] = 'davidb@example.com'
print("After adding email:", user_dictionary)
# Update a value
user_dictionary['age'] = 33
print("After updating age:", user_dictionary)
# Remove a key-value pair
user_dictionary.pop('name')
print("After removing name:", user_dictionary)

# Print all keys
print("Keys:", list(user_dictionary.keys()))
# Print all values
print("Values:", list(user_dictionary.values()))
# Print key-value pairs
for key, value in user_dictionary.items():
    print(f"{key}: {value}")

# Add user input to dictionary
key = input("Enter a key to add: ")
value = input("Enter a value for the key: ")
user_dictionary[key] = value
print("Updated dictionary:", user_dictionary)