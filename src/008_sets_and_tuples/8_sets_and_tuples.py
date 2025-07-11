# Working with sets
my_set = {1, 2, 3, 4, 5, 1, 2}  # Create a set (duplicates are removed)
print(my_set)
print(f"Set length: {len(my_set)}")  # Check length
for x in my_set:  # Iterate through set
    print(x)
my_set.discard(3)  # Remove 3
print(my_set)
my_set.add(6)  # Add 6
print(my_set)
my_set.update([7, 8])  # Add multiple items
print(my_set)
other_set = {5, 6, 9}  # Create another set
combined = my_set.union(other_set)  # Combine sets with union
print(f"Union: {combined}")
common = my_set.intersection(other_set)  # Find common items
print(f"Intersection: {common}")
diff = my_set.difference(other_set)  # Find items in my_set but not other_set
print(f"Difference: {diff}")
sym_diff = my_set.symmetric_difference(other_set)  # Find items in either set but not both
print(f"Symmetric difference: {sym_diff}")
new_item = int(input("Enter a number to add to the set: "))  # Add item from user input
my_set.add(new_item)
print(f"Updated set: {my_set}")

# Working with tuples
my_tuple = (1, 2, 3, 4, 5)  # Create a tuple
print(f"Second item: {my_tuple[1]}")  # Access second item
print(f"Sliced tuple: {my_tuple[1:3]}")  # Slice items from index 1 to 2
a, b, c, d, e = my_tuple  # Unpack tuple into variables
print(f"Unpacked: {a}, {b}, {c}, {d}, {e}")
nested_tuple = (1, (2, 3), 4)  # Create a nested tuple
print(f"Nested tuple: {nested_tuple}")
print(f"Inner tuple: {nested_tuple[1]}")  # Access inner tuple
# Note: Tuples are immutable, so my_tuple[1] = 100 would cause an error