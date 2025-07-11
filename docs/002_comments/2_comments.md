# Chapter 2: Comments

Comments are notes in your code that Python ignores when running the program. They help explain what the code does, making it easier to understand. You can write comments on one line or across multiple lines.

## Key Concepts
- **Single-Line Comments**: Use `#` to write a comment that takes up one line.
- **Multi-Line Comments**: Use triple quotes (`"""` or `'''`) to write comments that span multiple lines.
- **Commenting Out Code**: Use comments to temporarily disable code without deleting it.

## Code Examples
See [src/2_comments.py](../../src/002_comments/2_comments.py) for the full code.

1. **Single-Line Comments**  
   A comment can describe or disable a single line of code.

   ```python
   # Going to print hello world!
   # print("Hello World")
   print("Hi David")
   ```

   Output: `Hi David`

2. **Multi-Line Comments with #**  
   Multiple `#` lines can be used for longer comments.

   ```python
   # This is going over
   # Multiple
   # Lines
   ```

   Output: (No output, as it’s just comments)

3. **Multi-Line Comments with Triple Quotes**  
   Triple quotes (`"""` or `'''`) allow comments across multiple lines.

   ```python
   """
   This is going over
   multiple 
   lines
   """
   '''
   This is going over
   multiple 
   lines
   '''
   ```

   Output: (No output, as it’s just comments)