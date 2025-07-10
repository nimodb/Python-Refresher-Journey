# Define the list
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# Initialize counter for while loop
count = 0
# Repeat 3 times
while count < 3:
    # Iterate over list
    for day in my_list:
        if day == "Monday":
            continue  # Skip Monday
        print(day)
    count += 1