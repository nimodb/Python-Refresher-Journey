# Chapter 1: Variables

Variables store data in a program, like names or numbers. You can assign values to variables using `=` and change them later. Python lets you use variables in calculations or display them in text.

## Key Concepts
- **Creating Variables**: Assign a value to a variable name, e.g., `username = "davidbowie"`.
- **Using Variables**: Combine variables in strings with `f` strings, like `f"Hello {name}"`.
- **Calculations**: Use variables for math, e.g., multiplying or adding numbers.
- **Updating Variables**: Reassign a new value to a variable, and it replaces the old one.

## Code Examples
See [src/1_variables.py](src/1_variables.py) for the full code.

1. **Storing and Displaying Text**  
   Variables can hold text (strings) and be used in messages.

   ```python
   username = "davidbowie"
   first_name = "David"
   print(f"Hello {first_name}, your username is {username}")
   ```

   Output: `Hello David, your username is davidbowie`

2. **Calculating Prices**  
   Variables can store numbers and be used for calculations, like adding tax to a cost.

   ```python
   cost = 10
   tax_percent = 0.25
   tax = cost * tax_percent
   price = cost + tax
   print(f"Cost: {cost}, Tax: {tax}, Price: {price}")
   ```

   Output: `Cost: 10, Tax: 2.5, Price: 12.5`

3. **Updating Variables**  
   You can change a variable’s value by assigning a new one.

   ```python
   first_num = 10
   print(first_num)
   first_num = 30
   print(first_num)
   country = "Deutschland"
   print(country)
   country = "Iran"
   print(country)
   ```

   Output:
   ```
   10
   30
   Deutschland
   Iran
   ```