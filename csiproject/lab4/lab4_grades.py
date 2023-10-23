# Converts a number grade (an integer from 0 to 100) into a letter grade

grade = float(input("Enter your grade (0-100):"))  # Taking a grade, acounting for decimal grades

# Top down, determining grade
if grade >= 93:
    print("A")
elif grade >= 90:
    print("A-")
elif grade >= 87:
    print("B+")
elif grade >= 83:
    print("B")
elif grade >= 80:
    print("B-")
elif grade >= 77:
    print("C+")
elif grade >= 73:
    print("C")
elif grade >= 70:
    print("C-")
elif grade >= 67:
    print("D+")
elif grade >= 63:
    print("D")
elif grade >= 60:
    print("D-")
else:  # If no other letter grade is possible
    print("F")
