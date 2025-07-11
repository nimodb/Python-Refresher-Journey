# Get grade from user
try:
    grade = int(input("Enter your grade (0-100): "))
    # Check grade ranges and print letter grade
    if 90 <= grade <= 100:
        print("A")
    elif 80 <= grade <= 89:
        print("B")
    elif 70 <= grade <= 79:
        print("C")
    elif 60 <= grade <= 69:
        print("D")
    elif 0 <= grade <= 59:
        print("F")
    else:
        print("Error: Grade must be between 0 and 100")
except ValueError:
    print("Error: Please enter a valid integer")