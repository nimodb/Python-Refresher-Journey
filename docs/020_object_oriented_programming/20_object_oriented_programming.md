# Understanding Objects in Programming

This chapter introduces objects, the foundation of object-oriented programming (OOP), and explains how to model real-world things in Python using objects with properties and actions.

## What Are Objects?
Objects represent real-world items or ideas in a program. They can be physical things like a car or abstract concepts like a bank account. OOP uses objects to organize code.

### Examples of Real-World Objects
You can model many things as objects, such as:
- Trees
- Houses
- Cars
- Birds

Each object has specific traits and actions.

## Defining Objects
Objects have two main parts:
1. **Actions (Behaviors)**: What the object can do (e.g., a car can drive).
2. **Properties (State)**: Details that describe the object (e.g., a car’s color).

### Example: Car Object
Let’s look at a car as an object.

#### Car Actions
A car can:
- Accelerate
- Brake
- Turn
- Honk
- Start or stop its engine

#### Car Properties
- **Make**: The brand (e.g., Toyota, Ford)
- **Model**: The specific type (e.g., Corolla, Mustang)
- **Color**: The car’s color (e.g., Blue, Red)
- **Type**: The vehicle type (e.g., Sedan, SUV)
- **Fuel Type**: The fuel it uses (e.g., Gasoline, Electric)
- **Current Speed**: How fast it’s going (e.g., 60 mph)
- **Fuel Level**: How much fuel is left (e.g., 75%)

By defining a car’s state and behaviors, we can create programs that mimic real-world actions.

## Example: Dog Object
Here’s how to create a `Dog` object in Python to show state and behavior.

### Python Code
#### File: `src/020_object_oriented_programming/Dog.py`

```python
class Dog:
    def __init__(self):
        self.legs: int = 4
        self.ears: int = 2
        self.type: str = 'GoldenDoodle'
        self.age: int = 5
        self.color: str = 'Yellow'

    def bark(self) -> None:
        print("Woof! Woof!")

    def run(self) -> None:
        print("The dog is running!")
```

#### File: `src/020_object_oriented_programming/Main.py`
```python
from Dog import Dog

# Create a Dog object
dog = Dog()

# Access the dog's state (attributes)
print(f"Legs: {dog.legs}")
print(f"Ears: {dog.ears}")
print(f"Type: {dog.type}")
print(f"Age: {dog.age}")
print(f"Color: {dog.color}")

# Call the dog's behaviors (methods)
dog.bark()
dog.run()
```

### Explanation
- **State**: The `Dog` class defines attributes like `legs`, `ears`, `type`, `age`, and `color` to represent the dog’s properties.
- **Behavior**: Methods like `bark()` and `run()` define actions the dog can perform.
- **Instantiation**: In `Main.py`, a `Dog` object is created, and its attributes and methods are accessed.

## The Four Pillars of Object-Oriented Programming
OOP is built on four fundamental principles that guide how objects are designed and interact:
1. **Encapsulation**: Bundling data (attributes) and methods (behaviors) into a single unit (class) while restricting access to some components to protect the object’s integrity.
2. **Abstraction**: Hiding complex implementation details and exposing only the necessary features of an object to simplify its use.
3. **Inheritance**: Allowing a class to inherit attributes and methods from another class, promoting code reuse and hierarchy.
4. **Polymorphism**: Enabling objects of different classes to be treated as objects of a common superclass, often through method overriding or overloading.

## Project: Enemy Battle Game
In this project, we will create a small game where enemies fight each other, applying the four pillars of OOP to model their interactions.

### What’s the Goal?
Create a game where different enemies (like zombies or heroes) battle, each with unique traits and abilities.

#### Requirements
- Enemies can fight each other.
- Enemy types include:
  - Zombie
  - Ogre
  - Hero
- Each enemy has:
  - Health points
  - Attack damage
  - Special abilities

### Using OOP
We’ll apply the four principles:
1. **Encapsulation**: Group each enemy’s properties (like health) and actions (like attacking) in a class.
2. **Abstraction**: Show only key actions (like attacking) and hide internal details.
3. **Inheritance**: Use a base `Enemy` class for shared traits, with specific types like `Zombie` or `Hero` building on it.
4. **Polymorphism**: Let each enemy type have its own version of actions like attacking.

### Starting Point
To begin, we define a base `Enemy` class with core attributes and demonstrate its use.

#### File: `Enemy.py`
```python
class Enemy:
    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1
```

#### File: `Main.py`
```python
from Enemy import Enemy

# Create an Enemy object
enemy = Enemy(type_of_enemy="Zombie")

# Display enemy attributes
print(f"{enemy.type_of_enemy} has {enemy.health_points} health points and can deal {enemy.attack_damage} attack damage.")
```

#### Explanation
- **State**: The `Enemy` class defines attributes like `type_of_enemy`, `health_points`, and `attack_damage`.
- **Instantiation**: In `Main.py`, a `Zombie` enemy is created with default health points (10) and attack damage (1).
- **Future Steps**: Extend the `Enemy` class with behaviors (e.g., attack methods) and create subclasses for specific enemy types to implement unique abilities.

This foundation sets the stage for building a fully functional enemy battle game using OOP principles.


## Conclusion
By understanding objects through their state and behavior, and applying the four pillars of OOP, you can create robust, modular, and reusable code that effectively models real-world entities.