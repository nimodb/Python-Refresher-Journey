# Chapter 4: Getting User Input

User input allows programs to collect information from users during execution. The `input()` function prompts users to type data, which can be stored in variables and used in the program.

## Key Concepts
- **Using input()**: The `input()` function displays a prompt and waits for the user to type a response, which is returned as a string.
- **Combining with String Formatting**: Input data can be used in f-strings to create personalized messages.

## Code Examples
See [src/5_getting_user_input.py](../../src/005_getting_user_input/5_getting_user_input.py) for the full code.

1. **Collecting and Using User Input**  
   Prompt the user for their name and a number, then use the input in a formatted string.

   ```python
   first_name = input("Enter your first name: ")
   days = input("How many days before your birthday: ")
   print(f"Hi {first_name}, only {days} days before your birthday!")
   ```

   Example Output (if user enters "David" and "10"):
   ```
   Enter your first name: David
   How many days before your birthday: 10
   Hi David, only 10 days before your birthday!
   ```