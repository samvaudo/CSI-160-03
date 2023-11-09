#Data Validation

var = 'Here is some string data with the number two in it'
pswd = 'asd213#!sd09'
num = 23423
num2 = '23423.467'
space = '      '
name = 'John Doe'

'''
isalpha(): only alphabet characters
isspace(): only spaces
isdecimal(): is a decimal number
isalnum(): is alpha-numeric
istitle(): all words start with an uppercase
'''

'''
print("Is alpha:",var.isalpha())
print("Is a space:",var.isspace())
print("Is a decimal:",str(num).isdecimal())
#print(float(num2))
print("Is alphanumeric:",var.isalnum())
print("Full Name:",name.istitle())
'''
#VALIDATION FUNCTIONS
'''
# startswith() and endswith()
course = 'CSI-160'
if course.startswith('CSI') and course.endswith('160'):
    print('Valid Course.')
else:
    print('Course is not valid.')

isValid = False
for i in var:
    if i.isalpha() or i.isspace():
        isValid = True
    else:
        isValid = False
        break
if isValid:
    print('Valid input.')
else:
    print('Data integrity issues.')
'''

'''
Password Validator
1. Must be 8-12 characters long
2. At least 1 uppercase latter
3. At least 1 lowercase letter
4. At least 1 number
5. At least 1 valid character
'''
def paswd_validator():
    chars = ['@','%','*','$','#'] #valid special character
    password = input('Enter a password:')
    length = len(password)
    if length < 8 or length > 12:
        print('Invalid password: please enter a 8-12 characters')
        paswd_validator()
    else:
        has_upper = False
        has_lower = False
        has_special = False
        has_number = False
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char in chars:
                has_special = True
            elif char.isdigit():
                has_number = True
            else:
                continue
        if has_upper and has_lower and has_special and has_number:
            print("Valid Password!")
        else:
            print('Invalid password: Not complex enough')


paswd_validator()