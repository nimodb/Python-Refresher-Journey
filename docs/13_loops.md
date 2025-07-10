# Chapter 9: Loops

Loops let you repeat code multiple times. Python has two main types: `for` loops (for iterating over a sequence) and `while` loops (for repeating until a condition is false).

## Key Concepts
- **For Loop**: Iterates over a sequence (like a list or range) to process each item.
- **Range**: Generates numbers to loop over (e.g., `range(5)` gives 0 to 4).
- **While Loop**: Repeats code as long as a condition is true.
- **Loop Control**: Use `continue` to skip an iteration or `break` to exit the loop early.
- **Else with While**: Runs a block of code when the loop condition becomes false, unless broken.

## Code Examples
See [src/13_loops.py](src/13_loops.py) for the full code.

1. **For Loop with a List**  
   Iterate over a list to print each element.

   ```python
   # Create a list
   my_list = [1, 2, 3, 4, 5]
   # Print each element
   for num in my_list:
       print(num)
   ```

   Output:
   ```
   1
   2
   3
   4
   5
   ```

2. **For Loop with Range**  
   Use `range()` to iterate over numbers.

   ```python
   # Loop from 0 to 4
   for x in range(5):
       print(x)
   ```

   Output:
   ```
   0
   1
   2
   3
   4
   ```

3. **Summing a List with For Loop**  
   Calculate the sum of list elements.

   ```python
   # Create a list
   my_list = [1, 2, 3, 4, 5]
   # Sum elements
   sum_of_list = 0
   for x in my_list:
       sum_of_list += x
   print("Sum of list:", sum_of_list)
   ```

   Output:
   ```
   Sum of list: 15
   ```

4. **While Loop with Control Statements**  
   Use a `while` loop with `continue` and `break`.

   ```python
   # Initialize counter
   i = 0
   # Loop until i is 5
   while i < 5:
       i += 1
       if i == 3:
           continue  # Skip printing 3
       print(i)
       if i == 4:
           break  # Exit loop at 4
   else:
       print("i is now larger or equal to 5")
   ```

   Output:
   ```
   1
   2
   4
   ```