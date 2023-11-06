#Understanding scope in a Python file

x = 0  #Global variable
def my_function():
    global x
    x += 1
    y = 5 #Local variable, bound to the function
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

    inner_function()

outer_function()

