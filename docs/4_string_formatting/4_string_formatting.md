# Chapter 3: String Formatting

String formatting lets you insert variables into strings to create dynamic messages. Python offers different ways to format strings, such as using `.format()` or f-strings.

## Key Concepts
- **Using .format()**: Place `{}` in a string and use `.format()` to fill in variable values.
- **Using f-strings**: Add an `f` before a string and insert variables directly inside `{}` for a simpler approach.

## Code Examples
See [src/4_string_formatting.py](../../src/4_string_formatting/4_string_formatting.py) for the full code.

1. **Formatting with .format()**  
   Use `{}` as placeholders in a string and fill them with variables using `.format()`.

   ```python
   first_name = "David"
   sentence = "Hi {} {}"
   last_name = "Bowie"
   print(sentence.format(first_name, last_name))
   ```

   Output: `Hi David Bowie`

2. **Formatting with f-strings**  
   Use f-strings to directly embed variables inside `{}` in a string.

   ```python
   first_name = "David"
   last_name = "Bowie"
   print(f"Hi {first_name} {last_name} I am still listening to your music")
   ```

   Output: `Hi David Bowie I am still listening to your music`