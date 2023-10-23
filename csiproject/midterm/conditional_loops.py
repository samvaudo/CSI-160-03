# MIDTERM - Sam Vaudo

numbers = [1, 2, 7, 9, 13, 45, 3, 15, 6, 21]

saved_numbers = tuple(numbers)

# Lists needed
div_by_three = []
no_div = []


def divide_nums():
    for i in numbers:
        if i % 3 == 0:  # If divisible by 3
            div_by_three.append(i)
        else:  # If not divisible by 3
            no_div.append(i)
    print("numbers = ", numbers)
    print("div_by_three =", div_by_three)
    print("no_div =", no_div)
    print("saved_numbers =", saved_numbers)


divide_nums()
