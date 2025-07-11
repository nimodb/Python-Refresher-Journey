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