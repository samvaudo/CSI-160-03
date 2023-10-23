# Working with f_strings (format strings)\
import math
import random
import datetime  # This method fails
from datetime import datetime  # This makes the datetime module available to the interpeter

import replit


name = "Jane"
age = 25

x = random.randint(1, 5)
print(x)


def format_intro():
    print("Hello, {}! You're {} years old.".format(name, age))
    print("Hello,", name + "! You're", age, "years old.")


# format_intro()


def dict_intro():
    my_dictionary = {'name': 'John', 'name': 'Jane'}  # {key:value}
    print(my_dictionary)


# dict_intro()

# Modulo Operator, %
def mod_intro():
    print("Hello %s!" % name)
    date1 = '10/23/2023'
    date2 = '10-23-2023'
    date3 = "October 23, 2023"

# mod_intro()
