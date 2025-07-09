# Chapter 6: Sets and Tuples

Sets and tuples are collections of data, like lists, but with unique properties. Sets are unordered and don’t allow duplicates, while tuples are ordered and immutable (cannot be changed after creation).

## Key Concepts
### Sets
- **Creating Sets**: Use curly brackets `{}` to create a set, automatically removing duplicates.
- **Set Operations**: Use methods like `add()`, `discard()`, `update()`, `union()`, `intersection()`, `difference()`, or `symmetric_difference()` to work with sets.
- **Set Length**: Use `len()` to count items in a set.
- **Iterating Sets**: Use a `for` loop to access each item in a set.
- **User Input for Sets**: Use `input()` to let users add items to a set.
### Tuples
- **Creating Tuples**: Use parentheses `()` to create a tuple, which can’t be modified.
- **Accessing Tuples**: Use indexing (e.g., `tuple[1]`) or slicing (e.g., `tuple[1:3]`) to get items, or tuple unpacking to assign items to variables.
- **Nested Tuples**: Tuples can contain other tuples for complex data.
- **Tuple Immutability**: Tuples cannot be changed after creation (e.g., cannot assign new values).

## Code Examples
See [src/8_sets_and_tuples.py](src/8_sets_and_tuples.py) for the full code.

1. **Working with Sets**  
   Create a set, modify it, and perform operations like union, intersection, and difference.

   ```python
   # Create a set (duplicates are removed)
   my_set = {1, 2, 3, 4, 5, 1, 2}
   print(my_set)
   # Check length
   print(f"Set length: {len(my_set)}")
   # Iterate through set
   for x in my_set:
       print(x)
   # Remove 3
   my_set.discard(3)
   print(my_set)
   # Add 6
   my_set.add(6)
   print(my_set)
   # Add multiple items
   my_set.update([7, 8])
   print(my_set)
   # Combine sets with union
   other_set = {5, 6, 9}
   combined = my_set.union(other_set)
   print(f"Union: {combined}")
   # Find common items with intersection
   common = my_set.intersection(other_set)
   print(f"Intersection: {common}")
   # Find items in my_set but not other_set
   diff = my_set.difference(other_set)
   print(f"Difference: {diff}")
   # Find items in either set but not both
   sym_diff = my_set.symmetric_difference(other_set)
   print(f"Symmetric difference: {sym_diff}")
   # Add item from user input
   new_item = int(input("Enter a number to add to the set: "))
   my_set.add(new_item)
   print(f"Updated set: {my_set}")
   ```

   Example Output (if user enters "10"):
   ```
   {1, 2, 3, 4, 5}
   Set length: 5
   1
   2
   3
   4
   5
   {1, 2, 4, 5}
   {1, 2, 4, 5, 6}
   {1, 2, 4, 5, 6, 7, 8}
   Union: {1, 2, 4, 5, 6, 7, 8, 9}
   Intersection: {5, 6}
   Difference: {8, 1, 2, 4, 7}
   Symmetric difference: {1, 2, 4, 7, 8, 9}
   Enter a number to add to the set: 10
   Updated set: {1, 2, 4, 5, 6, 7, 8, 10}
   ```

2. **Working with Tuples**  
   Create a tuple, access items, and use slicing, unpacking, and nested tuples.

   ```python
   # Create a tuple
   my_tuple = (1, 2, 3, 4, 5)
   # Access second item
   print(f"Second item: {my_tuple[1]}")
   # Slice items from index 1 to 2
   print(f"Sliced tuple: {my_tuple[1:3]}")
   # Unpack tuple into variables
   a, b, c, d, e = my_tuple
   print(f"Unpacked: {a}, {b}, {c}, {d}, {e}")
   # Create a nested tuple
   nested_tuple = (1, (2, 3), 4)
   print(f"Nested tuple: {nested_tuple}")
   # Access inner tuple
   print(f"Inner tuple: {nested_tuple[1]}")
   # Note: Tuples are immutable, so my_tuple[1] = 100 would cause an error
   ```

   Output:
   ```
   Second item: 2
   Sliced tuple: (2, 3)
   Unpacked: 1, 2, 3, 4, 5
   Nested tuple: (1, (2, 3), 4)
   Inner tuple: (2, 3)
   ```