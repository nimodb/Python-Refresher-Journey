# Basic function
def greet():
    """Print a greeting message."""
    print("Hello, this is my function!")
greet()

# Function with parameters
def print_name(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")
print_name("Nimo", "DB")

# Function with local scope
def print_color_red():
    color = "red"
    print(f"The color is {color}.")
color = "blue"
print(f"The color is {color}.")
print_color_red()

# Function with named arguments
def print_numbers(highest_number, lowest_number):
    print(f"The highest number is {highest_number} and the lowest number is {lowest_number}.")
print_numbers(lowest_number=1, highest_number=10)

# Function with return value
def multiply_numbers(number1, number2):
    return number1 * number2
result = multiply_numbers(5, 10)
print(f"The result of multiplication is: {result}")

# Function with list parameter
def print_list_items(items):
    for item in items:
        print(f"Item: {item}")
my_list = ["apple", "banana", "cherry"]
print_list_items(my_list)

# Nested functions for tax calculation
def buy_item(cost):
    """Calculate total cost including tax."""
    return cost + add_tax(cost)
def add_tax(cost):
    """Calculate tax amount based on a 3% tax rate."""
    tax_rate = 0.03
    return cost * tax_rate
final_cost = buy_item(50)
print(f"Total cost with tax: ${final_cost}")