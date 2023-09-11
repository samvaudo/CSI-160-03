#how to work with functions

x1 = 0 #This is a gobal variable, it is avaiable for use by ALL FUNCTIONS
y1 = "" #Also a global variable

def more_vars():
    x2 = 5 #local variable
    y2 = 6 #local variable
    z = x2 + y2
    z2 = x1 + y2
    print(z)
    print(z2)
more_vars()

def CountNumbers():
    pass
#CountNumbers() #calls function

def var_mgt():
    global x #This makes the global variable available for anything, including reassignment of its value.
    print(x)
    x = x + 1 #This is trying to reassign the value of a global variable, the interpreter prevents this
    z = x + 2
    print(z) #The variable 'z' is a local variable. Its value is only available to this function

#var_mgt()

def add_numbers():
    print("The varialble 'x' equals:",x)
    num1 = x + 2
    print("The variable 'x' equals",x,"and num1 equals",num1)
    #print(z) The variable 'z' is not available to this function
#add_numbers()