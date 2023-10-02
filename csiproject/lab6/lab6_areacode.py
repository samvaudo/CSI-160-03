# Lab #6 area code appender

def add_area_code(phone_numbers, area_code):
    """Returns a list of phone numbers with the area code added.
    Given a list of phone numbers that are missing the area code,
    append the area code to the phone numbers in the list and return the result list.

    :param phone_numbers: (list) A list of phone numbers (strings) that do not have the area code
                                Example: ['555-1212']
    :param area_code: (str) The area code to add Example: '802'
    :return: (list) A list of phone numbers with the area code Example: ['802-555-1212']
    """
    temp_phone_numbers = phone_numbers
    for i in range(len(temp_phone_numbers)):
        temp_phone_numbers[i] = str(area_code)+'-'+temp_phone_numbers[i]

    return temp_phone_numbers

# example usage
phone_numbers = ['555-1212', '999-0738']
with_area_code = add_area_code(phone_numbers, '802')
print(with_area_code)
