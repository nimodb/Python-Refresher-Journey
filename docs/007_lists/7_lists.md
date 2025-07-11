# Chapter 5: Lists

Lists are collections of data, like numbers or strings, stored in a single variable. You can add, remove, modify, or access items in a list using various methods.

## Key Concepts
- **Creating Lists**: Use square brackets `[]` to create a list with items, like numbers or strings.
- **Adding Items**: Use `append()` to add an item to the end or `insert()` to add at a specific position.
- **Removing Items**: Use `remove()` to delete a specific item or `pop()` to remove an item at an index.
- **Sorting Lists**: Use `sort()` to arrange items in ascending order.
- **Accessing Items**: Use indexing (e.g., `list[0]`) to get a specific item or slicing (e.g., `list[1:3]`) to get a range of items.
- **Checking Length**: Use `len()` to find the number of items in a list.
- **Checking Membership**: Use `in` to check if an item is in a list.
- **User Input**: Use `input()` to let users add items to a list.

## Code Examples
See [src/7_lists.py](../../src/007_lists/7_lists.py) for the full code.

1. **Working with a List of Numbers**  
   Create and modify a list of integers, then access items and check properties.

   ```python
   # Create a list of integers
   numbers = [80, 96, 72, 100, 8]
   print(numbers)
   # Add 1000 to the end
   numbers.append(1000)
   print(numbers)
   # Insert 1000 at index 2
   numbers.insert(2, 1000)
   print(numbers)
   # Remove 8
   numbers.remove(8)
   print(numbers)
   # Remove item at index 0
   numbers.pop(0)
   print(numbers)
   # Sort in ascending order
   numbers.sort()
   print(numbers)
   # Access first item
   print(f"First number: {numbers[0]}")
   # Access items from index 1 to 2
   print(f"Sliced numbers: {numbers[1:3]}")
   # Check length
   print(f"List length: {len(numbers)}")
   # Check if 100 is in the list
   print(f"Is 100 in the list? {100 in numbers}")
   ```

   Output:
   ```
   [80, 96, 72, 100, 8]
   [80, 96, 72, 100, 8, 1000]
   [80, 96, 1000, 72, 100, 8]
   [80, 96, 1000, 72, 100]
   [96, 1000, 72, 100]
   [72, 96, 100, 1000]
   First number: 72
   Sliced numbers: [96, 100]
   List length: 4
   Is 100 in the list? True
   ```

2. **Working with a List of Strings**  
   Create and modify a list of strings, then access items and check properties.

   ```python
   # Create a list of strings
   fruits = ["apple", "banana", "cherry"]
   print(fruits)
   # Add "date" to the end
   fruits.append("date")
   print(fruits)
   # Insert "blueberry" at index 1
   fruits.insert(1, "blueberry")
   print(fruits)
   # Remove "banana"
   fruits.remove("banana")
   print(fruits)
   # Remove item at index 0
   fruits.pop(0)
   print(fruits)
   # Sort in alphabetical order
   fruits.sort()
   print(fruits)
   # Access first item
   print(f"First fruit: {fruits[0]}")
   # Access items from index 0 to 1
   print(f"Sliced fruits: {fruits[0:2]}")
   # Check length
   print(f"List length: {len(fruits)}")
   # Check if "cherry" is in the list
   print(f"Is cherry in the list? {'cherry' in fruits}")
   ```

   Output:
   ```
   ['apple', 'banana', 'cherry']
   ['apple', 'banana', 'cherry', 'date']
   ['apple', 'blueberry', 'banana', 'cherry', 'date']
   ['apple', 'blueberry', 'cherry', 'date']
   ['blueberry', 'cherry', 'date']
   ['blueberry', 'cherry', 'date']
   First fruit: blueberry
   Sliced fruits: ['blueberry', 'cherry']
   List length: 3
   Is cherry in the list? True
   ```

3. **Adding Items with User Input**  
   Let the user add an item to a list using `input()`.

   ```python
   # Create a list and add user input
   colors = ["red", "blue"]
   print(f"Initial colors: {colors}")
   new_color = input("Enter a color to add: ")
   colors.append(new_color)
   print(f"Updated colors: {colors}")
   ```

   Example Output (if user enters "green"):
   ```
   Initial colors: ['red', 'blue']
   Enter a color to add: green
   Updated colors: ['red', 'blue', 'green']
   ```