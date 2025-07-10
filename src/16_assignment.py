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