# A program for adding two numbers, returning it being greater than 100 if so

num1 = float(input("Enter the first number to add:"))  # gathering both numbers
num2 = float(input("Enter the second number to add:"))

total = num1 + num2  # calculating the sum

if total > 100:  # determing if the number is greater than 100
    print("They add up to a big number")
else:
    print("They add up to", total)
