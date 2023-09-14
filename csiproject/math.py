#Working with the math module
import math

'''
pi = math.pi
pi2 = 22/7
print("The value of pi in the math module equals",pi)
print("Calculating pi equals",pi2)

num = float(input("Enter a number:"))
exp = float(input("Enter an exponent"))
result = math.pow(num,exp) #first value is a float or an integer, the second is an exponent
print(result)
'''
def abs_val():
    num = float(input("Enter a number:"))
    num1 = abs(num)
    print("The absolute value of",num,"equals",num1)

abs_val()


