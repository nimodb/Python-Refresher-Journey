# Assignment 5: Days of Week Loop

This assignment involves using loops to print elements of a list multiple times while skipping a specific element.

## Problem Description
- Given: `my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]`
- Create a `while` loop to print all elements of `my_list` three times.
- Use a `for` loop inside the `while` loop to print the elements.
- Skip printing "Monday" using a `continue` statement.

## Solution
See [src/14_assignment.py](../../src/14_assignment/14_assignment.py) for the full code.

The program:
1. Defines the list of days.
2. Uses a `while` loop with a counter to repeat three times.
3. Uses a `for` loop to iterate over the list, skipping "Monday" with `continue`.
4. Prints each element (except "Monday") in each iteration.

```python
# Define the list
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# Initialize counter for while loop
count = 0
# Repeat 3 times
while count < 3:
    # Iterate over list
    for day in my_list:
        if day == "Monday":
            continue  # Skip Monday
        print(day)
    count += 1
```

Example Output:
```
Tuesday
Wednesday
Thursday
Friday
Tuesday
Wednesday
Thursday
Friday
Tuesday
Wednesday
Thursday
Friday
```