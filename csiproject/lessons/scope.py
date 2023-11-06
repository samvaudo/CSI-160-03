#Understanding scope in a Python file
import my_module
x = 0 #global variable
def my_function():
    global x
    x += 1
    y = 5#local variable, bound to the function
    print(x)
    print(y)

#my_function()

#Encapulating scope

def outer_function():
    z = 2
    print(z)
    def inner_function():
        z = 0
        print(z)

    inner_function()#only runs if outer_function() "succeeds"

#outer_function()

def my_math():
    r = int(input("Radius:"))
    area = my_module.p*my_module.math.pow(r,2)
    print(area)

my_math()
print(dir(my_module))