# Assignment 6: Vehicle Dictionary Operations

This assignment involves manipulating a dictionary using iteration, copying, and modification operations.

## Problem Description
Given the dictionary:
```python
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
```
- Create a `for` loop to print all keys and values.
- Create a new variable `vehicle2` as a copy of `my_vehicle`.
- Add a new key `'number_of_tires'` to `vehicle2` with the value `4`.
- Delete the `'mileage'` key and value from `vehicle2`.
- Print just the keys from `vehicle2`.

## Solution
See [src/16_assignment.py](src/16_assignment.py) for the full code.

The program:
1. Defines the `my_vehicle` dictionary.
2. Uses a `for` loop with `items()` to print all keys and values.
3. Creates a copy of `my_vehicle` called `vehicle2` using `copy()`.
4. Adds the key `'number_of_tires'` with value `4` to `vehicle2`.
5. Removes the `'mileage'` key from `vehicle2` using `pop()`.
6. Prints all keys from `vehicle2` using `keys()`.

```python
# Define the dictionary
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

# Print all keys and values
for key, value in my_vehicle.items():
    print(f"{key}: {value}")

# Create a copy of the dictionary
vehicle2 = my_vehicle.copy()

# Add number_of_tires key
vehicle2["number_of_tires"] = 4

# Remove mileage key
vehicle2.pop("mileage")

# Print all keys from vehicle2
print("Vehicle2 keys:", list(vehicle2.keys()))
```

Example Output:
```
model: Ford
make: Explorer
year: 2018
mileage: 40000
Vehicle2 keys: ['model', 'make', 'year', 'number_of_tires']
```