# MIDTERM - Sam Vaudo

import math
import random

# Variables needed
p = math.pi


def random_num():
    r_num = random.randint(0, 5)  # Generating random number
    random_area = p * math.pow(r_num, 2)  # Calculating area
    print("The random module randomly calculated an area of", random_area)


random_num()


def see_name(user):
    print("Hello", str(user) + ", you have completed the midterm exam.")


def more_stuff():
    user_name = str(input("What is your name?:"))
    diameter = float(input("Enter the length of the diameter of a circle:"))
    radius = diameter / 2
    area = p * math.pow(radius, 2)
    print("Name:", user_name)
    print("Area of the circle with diameter", diameter, "is", area)
    see_name(user_name)


more_stuff()
