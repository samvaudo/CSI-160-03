#Working with conditionals

def TestThis(): #simple conditional structure
    x = 2
    gpa = 3.0
    if (x ==3):
        print(x)
    elif (gpa == 3):
        print("GPA equals",gpa)
    else:
        print("Failure")

TestThis()

def NextClass():
    name = input("What is your name?")
    if name != "":
        
        course = input("Have you taken CSI-160? (y/n)")
        grade = input("What was your GPA for CSI-160?")