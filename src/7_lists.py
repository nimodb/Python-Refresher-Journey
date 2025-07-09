# Working with a list of integers
numbers = [80, 96, 72, 100, 8]
print(numbers)  # Print initial list
numbers.append(1000)  # Add 1000 to the end
print(numbers)
numbers.insert(2, 1000)  # Insert 1000 at index 2
print(numbers)
numbers.remove(8)  # Remove 8
print(numbers)
numbers.pop(0)  # Remove item at index 0
print(numbers)
numbers.sort()  # Sort in ascending order
print(numbers)
print(f"First number: {numbers[0]}")  # Access first item
print(f"Sliced numbers: {numbers[1:3]}")  # Access items from index 1 to 2
print(f"List length: {len(numbers)}")  # Check length
print(f"Is 100 in the list? {100 in numbers}")  # Check if 100 is in the list

# Working with a list of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Print initial list
fruits.append("date")  # Add "date" to the end
print(fruits)
fruits.insert(1, "blueberry")  # Insert "blueberry" at index 1
print(fruits)
fruits.remove("banana")  # Remove "banana"
print(fruits)
fruits.pop(0)  # Remove item at index 0
print(fruits)
fruits.sort()  # Sort in alphabetical order
print(fruits)
print(f"First fruit: {fruits[0]}")  # Access first item
print(f"Sliced fruits: {fruits[0:2]}")  # Access items from index 0 to 1
print(f"List length: {len(fruits)}")  # Check length
print(f"Is cherry in the list? {'cherry' in fruits}")  # Check if "cherry" is in the list

# Adding items with user input
colors = ["red", "blue"]
print(f"Initial colors: {colors}")
new_color = input("Enter a color to add: ")
colors.append(new_color)
print(f"Updated colors: {colors}")