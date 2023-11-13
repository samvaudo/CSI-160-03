var = "Here is some string data with the number two in it"
pswd = "asd213#!sd09"
num = 23423
num2 = '23423.468'
space = '     '
fullname = 'John Doe'
book = 'Why I Love Python Programming'
# print(len(pswd))

'''
isupper() and islower()
'''
name = 'ABC'
names = 'asdasdasd'
# print(name.isupper()) #If all characters are upper case, Python prints True
# print(names.islower())

'''
String methods:
isalpha(): All alpha characters
isalnum(): Combination of alpha and numeric chars.
isdecimal(): Numeric values, not floating point values
isspace(): A space
istitle(): Each word begins with an upper case letter

print(var.isalpha())
print(space.isspace())
print(str(num).isdecimal())
print(float(num2))
print(var.isalnum())
print('Full Name:',fullname.istitle())
print(book.istitle())

#startswith() and endswith()
course = 'CSI-160'
if course.startswith('CSI') and course.endswith('160'):
    print("Valid course.")
else:
    print("Course number not valid.")

valid = False
for i in var:
    if i.isalpha() or i.isspace():
        valid = True
    else:
        valid = False
        break
if valid == True:
    print('Valid input')
else:
    print('Data integrity issues')
'''
'''
Password Validator
1. Must be 8 to 12 characters
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one number
5. At least one valid special character
'''


def pswd_validator():
    chars = ['@', '%', '*', '$', '#']  # Valid special characters
    has_upper = False
    has_lower = False
    has_num = False
    has_special = False
    password = input('Enter a password:')
    length = len(password)
    if length < 8 or length > 12:
        print('Invalid password, please enter 8 to 12 characters.')
        pswd_validator()
        exit()
    else:
        for k in password:
            if k.isupper():
                has_upper = True
            elif k.islower():
                has_lower = True
            elif k.isdigit():
                has_num = True
            elif k in chars:
                has_special = True
            else:
                continue

    if has_upper and has_lower and has_num and has_special:
        print('Valid password')
    else:
        print("Process failed")


pswd_validator()
