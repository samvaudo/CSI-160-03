# More list/tuples

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]]

print(numbers)

print(numbers[3][0])

for row in numbers:
    for column in row:
        print(column)

