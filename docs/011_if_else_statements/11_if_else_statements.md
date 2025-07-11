# Chapter 8: If-Else Statements

If-else statements let you make decisions in your program by running different code based on conditions. They use boolean expressions to decide which block of code to execute.

## Key Concepts
- **If Statement**: Runs a block of code if a condition is `True`.
- **Elif Statement**: Checks another condition if the previous `if` or `elif` is `False`.
- **Else Statement**: Runs a block of code if all previous conditions are `False`.
- **Conditions**: Use comparison or logical operators to create boolean conditions.

## Code Examples
See [src/11_if_else_statements.py](../../src/011_if_else_statements/11_if_else_statements.py) for the full code.

1. **Using If-Elif-Else for Time-Based Greetings**  
   Print a greeting based on the time of day.

   ```python
   # Set the hour
   hour = 21
   # Check time and print appropriate greeting
   if hour < 15:
       print("Good morning!")
   elif hour < 20:
       print("Good afternoon!")
   else:
       print("Good Night!")
   ```

   Output:
   ```
   Good Night!
   ```