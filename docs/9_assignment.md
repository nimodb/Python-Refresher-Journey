# Assignment 3: Zoo List Operations

This assignment involves manipulating a list of animals using various list operations.

## Problem Description
- Create a list of 5 animals called `zoo`.
- Delete the animal at index 3 (fourth item).
- Append a new animal to the end of the list.
- Delete the animal at the beginning of the list (index 0).
- Print all the animals in the list.
- Print only the first 3 animals.

## Solution
See [src/9_assignment.py](src/9_assignment.py) for the full code.

The program:
1. Creates a list of 5 animals.
2. Removes the animal at index 3 using `pop()`.
3. Adds a new animal to the end using `append()`.
4. Removes the first animal using `pop(0)`.
5. Prints the entire list.
6. Prints the first 3 animals using slicing.

```python
# Create a list of 5 animals
zoo = ["lion", "elephant", "zebra", "giraffe", "tiger"]
# Remove animal at index 3
zoo.pop(3)
# Add a new animal
zoo.append("bear")
# Remove animal at index 0
zoo.pop(0)
# Print all animals
print("All animals:", zoo)
# Print first 3 animals
print("First 3 animals:", zoo[:3])
```

Example Output:
```
All animals: ['elephant', 'zebra', 'tiger', 'bear']
First 3 animals: ['elephant', 'zebra', 'tiger']
```