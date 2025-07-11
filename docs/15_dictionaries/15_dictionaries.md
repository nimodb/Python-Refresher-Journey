# Chapter 10: Dictionaries

Dictionaries store data as key-value pairs, allowing you to access values using unique keys. They are created with curly brackets `{}` and are useful for organizing related data.

## Key Concepts
- **Creating Dictionaries**: Use `{}` with keys and values (e.g., `'key': value`).
- **Accessing Values**: Use the key in square brackets (e.g., `dict['key']`) or the `get()` method.
- **Modifying Dictionaries**: Add or update key-value pairs with assignment or `update()`, and remove pairs with `pop()` or `del`.
- **Iterating Dictionaries**: Use a `for` loop to access keys, values, or both with `keys()`, `values()`, or `items()`.
- **User Input**: Use `input()` to let users add or modify dictionary entries.

## Code Examples
See [src/15_dictionaries.py](../../src/15_dictionaries/15_dictionaries.py) for the full code.

1. **Creating and Accessing a Dictionary**  
   Create a dictionary and access its values.

   ```python
   # Create a dictionary
   user_dictionary = {
       'username': 'david_bowie',
       'name': 'David',
       'age': 32
   }
   # Access values
   print("Username:", user_dictionary['username'])
   print("Name:", user_dictionary.get('name'))
   ```

   Output:
   ```
   Username: david_bowie
   Name: David
   ```

2. **Modifying a Dictionary**  
   Add, update, and remove key-value pairs.

   ```python
   # Add a new key-value pair
   user_dictionary['email'] = 'davidb@example.com'
   print("After adding email:", user_dictionary)
   # Update a value
   user_dictionary['age'] = 33
   print("After updating age:", user_dictionary)
   # Remove a key-value pair
   user_dictionary.pop('name')
   print("After removing name:", user_dictionary)
   ```

   Output:
   ```
   After adding email: {'username': 'david_bowie', 'name': 'David', 'age': 32, 'email': 'davidb@example.com'}
   After updating age: {'username': 'david_bowie', 'name': 'David', 'age': 33, 'email': 'davidb@example.com'}
   After removing name: {'username': 'david_bowie', 'age': 33, 'email': 'davidb@example.com'}
   ```

3. **Iterating Over a Dictionary**  
   Loop through keys, values, or key-value pairs.

   ```python
   # Print all keys
   print("Keys:", list(user_dictionary.keys()))
   # Print all values
   print("Values:", list(user_dictionary.values()))
   # Print key-value pairs
   for key, value in user_dictionary.items():
       print(f"{key}: {value}")
   ```

   Output:
   ```
   Keys: ['username', 'age', 'email']
   Values: ['david_bowie', 33, 'davidb@example.com']
   username: david_bowie
   age: 33
   email: davidb@example.com
   ```

4. **Adding a Key-Value Pair with User Input**  
   Let the user add a new key-value pair.

   ```python
   # Add user input to dictionary
   key = input("Enter a key to add: ")
   value = input("Enter a value for the key: ")
   user_dictionary[key] = value
   print("Updated dictionary:", user_dictionary)
   ```

   Example Output (if user enters "city" and "Germany"):
   ```
   Enter a key to add: city
   Enter a value for the key: Germany
   Updated dictionary: {'username': 'david_bowie', 'age': 33, 'email': 'davidb@example.com', 'city': 'Germany'}
   ```