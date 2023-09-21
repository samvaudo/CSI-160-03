#Working with return key word

def calc1():
    base = 3
    height = 10
    area = 0.5*base*height
    print("The area of a triangle equals",area)

def calc2():
    base = 3
    height = 10
    area = 0.5*base*height
    return area

#calc1()
#print(calc2())

def askName():
    name = input("What is your name?")
    return name
#askName()
print(askName())
