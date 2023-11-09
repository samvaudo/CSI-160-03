#Working with try and except

def calc_reciprocal():
    try:
        x = int(input('Enter a number:'))
        y = 1/x
        print(y)
        print('Your calculation was completed.')
        answer = input('Do you want to try again? (y/n)')
    except Exception as e:
        print('Incorrect input:',e)
        calc_reciprocal()

calc_reciprocal()