# Chapter 11: Functions

Functions are reusable blocks of code that perform specific tasks. They can take inputs (parameters), process them, and optionally return results.

## Key Concepts
- **Defining Functions**: Use `def` to create a function with a name and optional parameters.
- **Calling Functions**: Run a function by using its name followed by parentheses.
- **Parameters**: Pass data to functions as arguments, including named arguments for flexibility.
- **Return Values**: Use `return` to send a result back from a function.
- **Docstrings**: Add documentation to functions using triple quotes (`"""`) to describe their purpose.
- **Scope**: Variables defined inside a function are local and don’t affect variables outside.
- **Nested Functions**: Call one function inside another to break down complex tasks.

## Code Examples
See [src/17_functions.py](src/17_functions.py) for the full code.

1. **Basic Function**  
   Define and call a simple function to print a greeting.

   ```python
   def greet():
       """Print a greeting message."""
       print("Hello, this is my function!")
   greet()
   ```

   Output:
   ```
   Hello, this is my function!
   ```

2. **Function with Parameters**  
   Use parameters to print a personalized greeting.

   ```python
   def print_name(first_name, last_name):
       print(f"Hello, {first_name} {last_name}!")
   print_name("Nimo", "DB")
   ```

   Output:
   ```
   Hello, Nimo DB!
   ```

3. **Function with Local Scope**  
   Show how local variables don’t affect global variables.

   ```python
   def print_color_red():
       color = "red"
       print(f"The color is {color}.")
   color = "blue"
   print(f"The color is {color}.")
   print_color_red()
   ```

   Output:
   ```
   The color is blue.
   The color is red.
   ```

4. **Function with Named Arguments**  
   Use named arguments to specify high and low numbers.

   ```python
   def print_numbers(highest_number, lowest_number):
       print(f"The highest number is {highest_number} and the lowest number is {lowest_number}.")
   print_numbers(lowest_number=1, highest_number=10)
   ```

   Output:
   ```
   The highest number is 10 and the lowest number is 1.
   ```

5. **Function with Return Value**  
   Return the result of multiplying two numbers.

   ```python
   def multiply_numbers(number1, number2):
       return number1 * number2
   result = multiply_numbers(5, 10)
   print(f"The result of multiplication is: {result}")
   ```

   Output:
   ```
   The result of multiplication is: 50
   ```

6. **Function with List Parameter**  
   Iterate over a list to print each item.

   ```python
   def print_list_items(items):
       for item in items:
           print(f"Item: {item}")
   my_list = ["apple", "banana", "cherry"]
   print_list_items(my_list)
   ```

   Output:
   ```
   Item: apple
   Item: banana
   Item: cherry
   ```

7. **Nested Functions for Tax Calculation**  
   Use a helper function to calculate tax within another function.

   ```python
   def buy_item(cost):
       """Calculate total cost including tax."""
       return cost + add_tax(cost)
   def add_tax(cost):
       """Calculate tax amount based on a 3% tax rate."""
       tax_rate = 0.03
       return cost * tax_rate
   final_cost = buy_item(50)
   print(f"Total cost with tax: ${final_cost}")
   ```

   Output:
   ```
   Total cost with tax: $51.5
   ```