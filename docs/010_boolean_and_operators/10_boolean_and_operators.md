# Chapter 7: Boolean and Operators

Booleans are values that are either `True` or `False`, used to evaluate conditions. Operators compare values or combine conditions to produce boolean results.

## Key Concepts
- **Comparison Operators**: Compare two values to return `True` or `False` (e.g., equal `==`, not equal `!=`, greater than `>`, less than `<`, etc.).
- **Logical Operators**: Combine boolean values using `and` (both true), `or` (at least one true), or `not` (reverses the value).
- **Use in Programs**: Operators help make decisions or check conditions in code.

## Code Examples
See [src/10_boolean_and_operators.py](../../src/010_boolean_and_operators/10_boolean_and_operators.py) for the full code.

1. **Comparison Operators**  
   Use operators to compare numbers and get boolean results.

   ```python
   # Check if 1 equals 2
   print(1 == 2)
   # Check if 1 is not equal to 2
   print(1 != 2)
   # Check if 1 is greater than 2
   print(1 > 2)
   # Check if 1 is less than 2
   print(1 < 2)
   # Check if 1 is greater than or equal to 1
   print(1 >= 1)
   # Check if 1 is less than or equal to 2
   print(1 <= 2)
   ```

   Output:
   ```
   False
   True
   False
   True
   True
   True
   ```

2. **Logical Operators**  
   Combine conditions to produce a single boolean result.

   ```python
   # Check if 1 > 3 and 5 < 7
   print(1 > 3 and 5 < 7)
   # Check if 1 > 3 or 5 < 7
   print(1 > 3 or 5 < 7)
   # Reverse the result of 1 == 1
   print(not(1 == 1))
   ```

   Output:
   ```
   False
   True
   False
   ```