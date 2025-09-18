# Constructors

This chapter explains constructors, which are special methods used to create and set up objects in a class.

## What Are Constructors?
A constructor is a method that runs automatically when you create a new object from a class. It sets up the object’s initial state, with or without starting values. In Python, the constructor is defined using the `__init__` method.

### Example: Creating an Enemy
Here’s an example from the previous chapter, updated to show a constructor in action:

#### File: `src/022_constructors/Enemy.py`
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

#### File: `src/022_constructors/Main.py`
```python
from Enemy import Enemy

# Create a Zombie enemy using the constructor
zombie = Enemy()
zombie.type_of_enemy = "Zombie"

# Use enemy methods
zombie.talk()
zombie.walk_forward()
zombie.attack()
```

### Explanation
- **Constructor Call**: The line `zombie = Enemy()` calls the `__init__` method (the constructor) to create a new `Enemy` object.
- **Initialization**: The `__init__` method sets default values for `type_of_enemy`, `health_points`, and `attack_damage`.
- **The `self` Parameter**: `self` refers to the object being created (e.g., `zombie`). It lets the constructor set properties like `self.type_of_enemy` for that specific object.

## Types of Constructors
There are three main types of constructors in Python:
1. **Default/Empty Constructor**
2. **No Argument Constructor**
3. **Parameter Constructor**

Let’s explore each type with examples.

### 1. Default/Empty Constructor
A default or empty constructor is automatically provided by Python if you don’t define an `__init__` method. It doesn’t set any properties or take arguments.

#### Example
```python
class EmptyEnemy:
    pass

# Create an object with the default constructor
enemy = EmptyEnemy()
print(enemy)  # Outputs: <__main__.EmptyEnemy object at ...>
```

**Explanation**:
- Python creates a basic object with no properties or methods.
- Useful for simple classes where no initial setup is needed.
- Rarely used in practice since it doesn’t initialize any state.

### 2. No Argument Constructor
A no argument constructor is an `__init__` method that takes only `self` and sets default values for the object’s properties.

#### Example
This is the constructor used in the `Enemy` class above:

```python
class Enemy:
    def __init__(self):
        self.type_of_enemy = ""
        self.health_points = 10
        self.attack_damage = 1

# Create an object with the no argument constructor
enemy = Enemy()
print(f"Type: {enemy.type_of_enemy}, HP: {enemy.health_points}, Damage: {enemy.attack_damage}")
```

**Explanation**:
- The `__init__` method sets default values (`""`, `10`, `1`) without requiring any input from the user.
- Useful when all objects start with the same initial state.
- The user can later change properties, like `enemy.type_of_enemy = "Zombie"`.

### 3. Parameter Constructor
A parameter constructor is an `__init__` method that takes arguments (besides `self`) to set the object’s initial properties.

#### Example
Let’s modify the `Enemy` class to use a parameter constructor:

#### File: `src/022_constructors/EnemyWithParams.py`
```python
class Enemy:
    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I am a {self.type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage")
```

#### File: `src/022_constructors/MainWithParams.py`
```python
from Enemy import Enemy

# Create a Zombie enemy using the parameter constructor
zombie = Enemy("Zombie", 15, 2)

# Use enemy methods
zombie.talk()
zombie.walk_forward()
zombie.attack()
```

**Explanation**:
- The `__init__` method takes `type_of_enemy`, `health_points`, and `attack_damage` as arguments.
- When creating the object (`zombie = Enemy("Zombie", 15, 2)`), you pass values to set the initial state.
- Useful when each object needs different starting values.
- Makes the code more flexible and avoids manually setting properties after creation.

## Why Use Constructors?
- **Initialization**: Constructors set up an object’s starting state, ensuring it’s ready to use.
- **Flexibility**: Parameter constructors allow custom values for each object.
- **Clarity**: No argument constructors provide consistent defaults, while parameter constructors make it clear what values are needed.
- **Scalability**: Constructors make it easier to create multiple objects with different properties in larger programs, like our enemy battle game.

Constructors are essential for creating objects efficiently and are a key part of object-oriented programming.