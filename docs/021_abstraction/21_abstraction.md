# Abstraction

This chapter explains abstraction, a key concept in object-oriented programming (OOP) that simplifies how we interact with objects by hiding complex details.

## What Is Abstraction?
Abstraction means showing only the essential features of an object to the user while hiding how it works behind the scenes. This makes code easier to use and understand.

### Example: Flashlight
Think of a flashlight:
- It has an "on" and "off" switch.
- When you turn it "on," a beam of light comes out.
- When you turn it "off," the light stops.
- You don’t need to know how the bulb or battery works inside—just that flipping the switch controls the light.

Abstraction lets you focus on what the flashlight does (produce light) without worrying about its internal mechanics.


### Python Code
#### File: `src/021_abstraction/Enemy.py`
```python
class Enemy:
    def __init__(self):
        self.type_of_enemy = ""
        self.health_points = 10
        self.attack_damage = 1

    def talk(self):
        print(f"I am a {self.type_of_enemy}. Be prepared to fight!")
```

#### File: `src/021_abstraction/Main.py`
```python
from Enemy import Enemy

# Create a Zombie enemy
enemy = Enemy()
enemy.type_of_enemy = "Zombie"

# Use the talk method
enemy.talk()
print(f"{enemy.type_of_enemy} has {enemy.health_points} health points and can deal {enemy.attack_damage} attack damage.")
```

### Explanation
- **Abstraction**: The `talk` method lets the enemy "speak" without showing how the message is created. The user only needs to call `enemy.talk()` to get the output.
- **The `self` Parameter**: In Python, `self` refers to the specific object (like a particular enemy) calling the method. For example, in `enemy.talk()`, `self` is the `enemy` object, letting the method access its properties like `type_of_enemy`. Every class method needs `self` as its first parameter to work with the object’s data.

## Expanding the Enemy Class
Let’s add more methods to the `Enemy` class to show how abstraction simplifies interactions.

#### Updated File: `src/021_abstraction/Enemy.py`
```python
class Enemy:
    def __init__(self):
        self.type_of_enemy = ""
        self.health_points = 10
        self.attack_damage = 1

    def talk(self):
        print(f"I am a {self.type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage")
```

#### Updated File: `src/021_abstraction/Main.py`
```python
from Enemy import Enemy

# Create a Zombie enemy
zombie = Enemy()
zombie.type_of_enemy = "Zombie"

# Use enemy methods
zombie.talk()
zombie.walk_forward()
zombie.attack()
```

### Explanation
- **New Methods**: The `walk_forward` and `attack` methods let the enemy perform actions. Users call these methods without needing to know how they’re coded.
- **Using `self`**: Each method uses `self` to access the enemy’s properties, like `type_of_enemy` or `attack_damage`. For example, `self.type_of_enemy` in `talk` ensures the correct enemy type is used (e.g., "Zombie").
- **Abstraction**: Users interact with simple method calls (`zombie.talk()`, `zombie.attack()`) while the internal logic stays hidden.

## Why Use Abstraction?
Abstraction has several benefits:
- **Simplicity**: Users don’t need to understand complex code to use an object’s features.
- **Reusable Code**: Methods like `talk` or `attack` can be used across different enemies.
- **DRY Principle**: Abstraction reduces repeated code (Don’t Repeat Yourself) by grouping functionality in one place.
- **Scalability**: Objects can be extended with new features without changing how users interact with them.

Abstraction makes code easier to use, maintain, and expand, especially in larger programs like our enemy battle game.