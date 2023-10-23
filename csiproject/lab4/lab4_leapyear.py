# Defines a function to determine if a year is a hebrew leap year

def is_hebrew_leap_year(year):
    remainder = year % 19  # getting the remainder
    if remainder in [0, 3, 6, 8, 11, 14, 17]:  # deteriming if the remainder is in the list given for leap years
        return True
    else:
        return False


print(is_hebrew_leap_year(5779))  # is a leap year

print(is_hebrew_leap_year(5781))  # is not a leap year
