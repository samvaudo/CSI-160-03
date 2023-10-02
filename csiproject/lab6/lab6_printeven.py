# print even numbers

def print_even(numbers):
    """Prints the even numbers in a list, one per line

    :param numbers: (list) list of integers
    :return: None
    """
    for i in numbers:
        if i%2==0:
            print(i)
    pass

print_even([1,2,3,4,5,6,7,10])