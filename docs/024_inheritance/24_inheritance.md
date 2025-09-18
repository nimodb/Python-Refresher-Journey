# Inheritance

This chapter explains inheritance, a key concept in object-oriented programming (OOP) that allows one class to acquire attributes and methods from another class, creating a hierarchy.

## What Is Inheritance?
Inheritance is the process where a child class (also called a subclass) gets properties (attributes) and behaviors (methods) from a parent class (also called a superclass). This creates a hierarchy between classes, promoting code reuse.

### Example: Animal and Dog Classes
The `Animal` class is the parent class with basic attributes.

#### File: `src/024_inheritance/Animal.py`
```python
class Animal:
    def __init__(self):
        self.weight = 0  # int
        self.color = ""  # str
        self.age = 0     # int
        self.animal_typ = ""  # str
```

The `Dog` class is the child class that inherits from `Animal`.

#### File: `src/024_inheritance/Dog.py`
```python
class Dog(Animal):
    def __init__(self):
        super().__init__()  # Inherit from Animal
        self.can_shed = False  # bool

    # Inherits all Animal attributes: weight, color, age, animal_typ
```

### Explanation
- The `Dog` class automatically gets all attributes from `Animal` (weight, color, age, animal_typ).
- `Dog` adds its own attribute: `can_shed`.
- This hierarchy allows `Dog` to reuse `Animal`'s properties without rewriting them.

## Adding Methods to the Parent Class
Let's add methods to the `Animal` class for common behaviors.

#### Updated File: `src/024_inheritance/Animal.py`
```python
class Animal:
    def __init__(self):
        self.weight = 0
        self.color = ""
        self.age = 0
        self.animal_typ = ""

    def eat(self):
        print("Animal eating.")

    def sleep(self):
        print("Animal sleeping.")
```

The `Dog` class now inherits these methods too.

#### Updated File: `src/024_inheritance/Dog.py`
```python
class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.can_shed = False

    # Inherits all Animal attributes and methods: eat(), sleep()

    def talk(self):
        print("Bark!")
```

### Demonstration
#### File: `src/024_inheritance/Main.py`
```python
from Dog import Dog

# Create a Dog object
dog = Dog()
dog.animal_typ = "Mammal"  # Inherited attribute
dog.can_shed = True        # Dog's own attribute

# Use inherited methods
dog.eat()   # Outputs: Animal eating.
dog.sleep() # Outputs: Animal sleeping.

# Use Dog's own method
dog.talk()  # Outputs: Bark!
```

### Explanation
- When you create a `Dog` object and call `dog.eat()`, it uses the method from the parent `Animal` class.
- `Dog` also has its own `talk()` method.

## What Is Method Overriding?
Method overriding happens when a child class provides its own version of a method that already exists in the parent class. If the child doesn't have the method, it uses the parent's version.

Let's override the `eat()` method in the `Dog` class.

#### Updated File: `src/024_inheritance/Dog.py`
```python
class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.can_shed = False

    def eat(self):  # Overrides Animal's eat()
        print("Dog eating.")

    def talk(self):
        print("Bark!")

    # Inherits sleep() from Animal
```

#### Updated File: `src/024_inheritance/Main.py`
```python
from Dog import Dog

# Create a Dog object
dog = Dog()

# Use overridden method
dog.eat()   # Outputs: Dog eating. (not Animal eating.)

# Use inherited method
dog.sleep() # Outputs: Animal sleeping.

# Use Dog's own method
dog.talk()  # Outputs: Bark!
```

### Explanation
- The `Dog` class now has its own `eat()` method, which overrides the parent's version.
- When calling `dog.eat()`, it uses the child's version.
- `sleep()` is not overridden, so it uses the parent's version.

## Adding Another Child Class: Bird
Now, let's create a `Bird` class that also inherits from `Animal`, adding it to the hierarchy.

#### File: `src/024_inheritance/Bird.py`
```python
class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.bird_type = ""  # str

    def talk(self):
        print("Chirp!")

    def fly(self):
        print("Bird begins to soar!")

    # Inherits all Animal attributes and methods: eat(), sleep()
```

#### Updated File: `src/024_inheritance/Main.py`
```python
from Dog import Dog
from Bird import Bird

# Create a Dog object
dog = Dog()
dog.eat()   # Outputs: Dog eating.
dog.talk()  # Outputs: Bark!

# Create a Bird object
bird = Bird()
bird.animal_typ = "Bird"  # Inherited attribute
bird.bird_type = "Eagle"  # Bird's own attribute

# Use inherited methods
bird.eat()   # Outputs: Animal eating.
bird.sleep() # Outputs: Animal sleeping.

# Use Bird's own methods
bird.talk()  # Outputs: Chirp!
bird.fly()   # Outputs: Bird begins to soar!
```

### Explanation
- The hierarchy now includes `Animal` (parent), `Dog` (child), and `Bird` (child).
- `Bird` inherits all `Animal` attributes and methods.
- `Bird` adds its own attributes (`bird_type`) and methods (`talk()`, `fly()`).
- Each child class can override methods or add new ones as needed.

Inheritance helps build organized, reusable code by sharing common features across related classes.