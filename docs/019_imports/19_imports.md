# Chapter 12: Imports

Imports allow you to use code from other Python files (modules) or the standard library to add functionality to your program.

## Key Concepts
- **Custom Modules**: Import functions or variables from your own Python files using `import module_name` or specific imports like `from module_name import function`.
- **Standard Library**: Use Python’s built-in modules (e.g., `random`, `math`) without installing anything.
- **Import Syntax**: Import entire modules or specific functions to reuse code efficiently.
- **Module Usage**: Call functions from imported modules to process data, like calculating averages or generating random values.

## Code Examples
See [src/019_imports/19_homework_grades.py](../../src/019_imports/19_homework_grades.py), [src/019_imports/19_standardlib.py](../../src/019_imports/19_standardlib.py), and [src/019_imports/grade_average_service.py](../../src/019_imports/grade_average_service.py) for the full code.

1. **Importing a Custom Module**  
   Import a function from a custom module to calculate the average of homework grades.

   ```python
   from grade_average_service import calculate_homework
   homework_assignment_grades = {
       'homework_1': 85,
       'homework_2': 100,
       'homework_3': 81
   }
   calculate_homework(homework_assignment_grades)
   ```

   Output:
   ```
   88.67
   ```

2. **Using Standard Library Modules**  
   Use `random` to pick a random item or number and `math` to calculate a square root.

   ```python
   import random
   types_of_drinks = ['Soda', 'Coffee', 'Water', 'Tea']
   print(random.choice(types_of_drinks))
   print(random.randint(1, 10))
   import math
   square_root = math.sqrt(64)
   print(square_root)
   ```

   Example Output (random output may vary):
   ```
   Water
   7
   8.0
   ```

3. **Custom Module Definition**  
   Define a function in a separate module to calculate the average of dictionary values.

   ```python
   def calculate_homework(homework_assignments):
       sum_of_grades = 0
       for homework in homework_assignments.values():
           sum_of_grades += homework
       final_grade = round(sum_of_grades / len(homework_assignments), 2)
       print(final_grade)
   ```