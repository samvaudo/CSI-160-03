"""DESCRIPTION OF THE MODULE GOES HERE

Author: Sam Vaudo
Class: CSI-160
Assignment: Lab-03
Due Date:9/22/2023

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

import math

pi = math.pi


def volume_sphere(r):
    """
    Calculates the volume of a sphere
    :param r: the radius of the sphere
    :return: the volume of the sphere, in the units of the radius cubed
    :Assumptions/Conditions: r is a positive int/float
    """
    if (type(r) is not int) & (type(r) is not float):
        return "Wrong data type. n should be a(n) integer or float"
    else:
        volume = (4 / 3) * pi * math.pow(r, 3)
        return volume


def volume_cylinder(r, h):
    """
    :Description:Calculates the volume of a cylinder
    :param r:radius of the circle for a cylinder
    :param h:height of the cylinder
    :return:the volume of the cylinder in the units of h cubed
    :Assumptions/Conditions:h and r are both positive ints and/or floats,h and r are the same units
    """
    if (type(r) is not int) & (type(r) is not float):
        return "Wrong data type. r should be a(n) integer or float"
    elif (type(h) is not int) & (type(h) is not float):
        return "Wrong data type. h should be a(n) integer or float"
    else:
        area = pi * math.pow(r, 2)
        volume = area * h
        return volume


def power_of_two(n):
    """
    :Description:calculates the nth power of two, where n is the exponent
    :param n: that is put to the power of two
    :return: The power of two to the power of n
    :Assumptions/Conditions:n is an int/float
    """
    if (type(n) is not int) & (type(n) is not float):
        return "Wrong data type. n should be a(n) integer or float"
    else:
        return math.pow(2, n)


# Running volume_sphere()
print("Volume of a sphere r = 4", volume_sphere(4))  # test with int
print("Volume of a sphere r = 4.5", volume_sphere(4.5))  # test with float
print("Testing string val\n", volume_sphere("abc"))  # test with str

print("Volume of a cylinder r = 4, h = 5", volume_cylinder(4, 5))  # test with int
print("Volume of a cylinder r = 4.5, h = 5.5", volume_cylinder(4.5, 5.5))  # test with float
print("Testing string val\n", volume_cylinder("a", "b"))  # test with str

print("2^n, n = 5 is", power_of_two(5))  # test with int
print("2^n, n = 5.5 is", power_of_two(5.5))  # test with float
print("Testing string val", power_of_two("5"))  # test with str
