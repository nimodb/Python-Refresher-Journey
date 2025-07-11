# Assignment 2: Birthday Weeks Calculation

This assignment involves writing a program to calculate the approximate number of weeks until a user’s birthday based on their input.

## Problem Description
- Ask the user how many days until their birthday.
- Calculate the approximate number of weeks by dividing the days by 7 (since 1 week equals 7 days).
- Print the result using the `print()` function.

## Solution
See [src/6_assignment.py](../../src/6_assignment/6_assignment.py) for the full code.

The program:
1. Prompts the user to enter the number of days until their birthday.
2. Converts the input (a string) to a number and divides it by 7 to get weeks.
3. Prints the approximate number of weeks.

```python
# Get days until birthday
days = input("How many days until your birthday: ")
# Convert to number and calculate weeks
weeks = int(days) / 7
# Display result
print(f"Your birthday is approximately {weeks} weeks away!")
```

Example Output (if user enters "21"):
```
How many days until your birthday: 21
Your birthday is approximately 3.0 weeks away!
```