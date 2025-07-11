# Assignment 4: Grade Calculator

This assignment involves using if-else statements to determine a letter grade based on a numeric grade.

## Problem Description
- Create a variable `grade` with an integer between 0 and 100.
- Use `if`, `elif`, `else` statements to print the corresponding letter grade:
  - A: 90–100
  - B: 80–89
  - C: 70–79
  - D: 60–69
  - F: 0–59
- Example: If `grade = 87`, print `B`.

## Solution
See [src/12_assignment.py](../../src/012_assignment/12_assignment.py) for the full code.

The program:
1. Prompts the user to enter a grade (0–100).
2. Checks if the input is valid using a `try/except` block.
3. Uses `if`, `elif`, `else` statements to determine and print the letter grade.

```python
# Get grade from user
try:
    grade = int(input("Enter your grade (0-100): "))
    # Check grade ranges and print letter grade
    if 90 <= grade <= 100:
        print("A")
    elif 80 <= grade <= 89:
        print("B")
    elif 70 <= grade <= 79:
        print("C")
    elif 60 <= grade <= 69:
        print("D")
    elif 0 <= grade <= 59:
        print("F")
    else:
        print("Error: Grade must be between 0 and 100")
except ValueError:
    print("Error: Please enter a valid integer")
```

Example Output (for valid input):
```
Enter your grade (0-100): 87
B
```

Example Output (for invalid input):
```
Enter your grade (0-100): abc
Error: Please enter a valid integer
```