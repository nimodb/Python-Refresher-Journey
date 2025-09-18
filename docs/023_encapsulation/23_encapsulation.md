# Encapsulation

This chapter explains encapsulation, a key concept in object-oriented programming (OOP) that groups data and methods together and controls access to them.

## What Is Encapsulation?
Encapsulation means bundling an object’s data (attributes) and methods (actions) into a single class, while controlling how others can access or modify that data. By making some attributes private, you can protect them from being changed directly, ensuring safer and more controlled interactions.

### Example: Enemy Attributes
The `Enemy` class from previous chapters has three attributes:
- `type_of_enemy`
- `health_points`
- `attack_damage`

By default, these attributes are **public**, meaning anyone can access or change them directly. This can lead to unexpected changes, like setting `health_points` to a negative value. To prevent this, we can make attributes **private** and use special methods to control access.

#### Making Attributes Private
In Python, we make an attribute private by adding a double underscore (`__`) before its name. Let’s make `type_of_enemy` private and keep `health_points` and `attack_damage` public. To allow controlled access to the private `type_of_enemy`, we create **getter** and **setter** methods.

#### Python Code
##### File: `src/023_encapsulation/Enemy.py`
```python
class Enemy:
    def __init__(self):
        self.__type_of_enemy = ""  # Private attribute
        self.health_points = 10    # Public attribute
        self.attack_damage = 1     # Public attribute

    # Getter method for type_of_enemy
    def get_type_of_enemy(self):
        return self.__type_of_enemy

    # Setter method for type_of_enemy
    def set_type_of_enemy(self, type_of_enemy):
        self.__type_of_enemy = type_of_enemy

    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage")
```

##### File: `src/023_encapsulation/Main.py`
```python
from Enemy import Enemy

# Create a Zombie enemy
zombie = Enemy()

# Set the private type_of_enemy using the setter
zombie.set_type_of_enemy("Zombie")

# Get the private type_of_enemy using the getter
print(f"Enemy type: {zombie.get_type_of_enemy()}")

# Use enemy methods
zombie.talk()
zombie.walk_forward()
zombie.attack()

# Try to access public attributes directly
print(f"Health: {zombie.health_points}, Damage: {zombie.attack_damage}")

# Try to access private attribute directly (will raise an error)
# print(zombie.__type_of_enemy)  # AttributeError
```

### Explanation
- **Public Attributes**: `health_points` and `attack_damage` are public, so they can be accessed directly (e.g., `zombie.health_points`).
- **Private Attribute**: `type_of_enemy` is private (`__type_of_enemy`), so it can’t be accessed directly (e.g., `zombie.__type_of_enemy` raises an error).
- **Getter Method**: `get_type_of_enemy()` returns the value of `__type_of_enemy`.
- **Setter Method**: `set_type_of_enemy()` allows controlled updates to `__type_of_enemy`.
- **The `self` Parameter**: `self` refers to the specific object (e.g., `zombie`) and is used to access or modify its attributes, like `self.__type_of_enemy` in the getter and setter.
- **Encapsulation**: By making `type_of_enemy` private and using getter/setter methods, we control how it’s accessed or changed, protecting the object’s data.

## Why Use Encapsulation?
Encapsulation offers several benefits:
- **Groups Related Data and Methods**: Keeps attributes and methods that belong together in one class.
- **Cleaner Code**: Makes code easier to read and understand by organizing data access.
- **Flexibility**: Allows controlled changes to data through getters and setters, which can include validation if needed.
- **Reusability**: Encapsulated classes can be reused across programs without exposing internal details.
- **Hides Sensitive Data**: Prevents direct access to private attributes, keeping them safe from unintended changes.

Encapsulation helps create secure, organized, and maintainable code, especially for projects like our enemy battle game.