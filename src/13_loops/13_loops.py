# Create a list
my_list = [1, 2, 3, 4, 5]
# Print each element using a for loop
for num in my_list:
    print(num)

# Loop from 0 to 4 using range
for x in range(5):
    print(x)

# Sum elements in the list
sum_of_list = 0
for x in my_list:
    sum_of_list += x
print("Sum of list:", sum_of_list)

# While loop with continue and break
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Skip printing 3
    print(i)
    if i == 4:
        break  # Exit loop at 4
else:
    print("i is now larger or equal to 5")