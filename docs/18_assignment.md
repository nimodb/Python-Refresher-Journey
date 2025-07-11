# Assignment 7: User Dictionary Creation

This assignment involves creating a function that builds a dictionary from input parameters.

## Problem Description
- Create a function that takes three parameters (`firstname`, `lastname`, `age`) and returns a dictionary with those values as key-value pairs.

## Solution
See [src/18_assignment.py](src/18_assignment.py) for the full code.

The program:
1. Defines a function `create_user` that takes `firstname`, `lastname`, and `age` as parameters.
2. Returns a dictionary with keys `'firstname'`, `'lastname'`, and `'age'` mapped to the input values.
3. Calls the function with sample inputs and prints the resulting dictionary.

```python
def create_user(firstname, lastname, age):
    """Create a dictionary from user details."""
    return {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }

# Create a dictionary with sample inputs
user = create_user("Nimo", "DB", 32)
print("User dictionary:", user)
```

Example Output:
```
User dictionary: {'firstname': 'Nimo', 'lastname': 'DB', 'age': 32}
```