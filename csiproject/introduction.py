#Day1
#this is a one line comment

'''
Here is a block comment
It supports multiple lines of comments
'''

"""
Same comment with double quotes
"""

'''
Rules for variable creation
1. Dont start with a number
    1a
        cant be a variable

2. No spaces
    my variable
        cant be a variable
3. No keywords
    print1
        cant be a variable

4. No special characters
    MyVarialbe!
        cant be a variable
'''

#a variable
#x1 = 1
#x2 = 4
#Why_not = "why not"
#FirstName = "Name"
#print = "hello world"

#result = x2 - x1
#print(result)
#Day 2
name = ""
age = 0
age = 22

user = "john doe"

#print("The user's nam is" user "who is" age "years old.")
#print("The user's name is "+user+" who is "+str(age)+" years old.")

"""
Converting commands
-int()
-str()
-float()
-len()
-input()

"""
grade1 = 3.25
grade2 = 3.75
grade3 = 3.5
grade4 = 3.25
grade5 = 0

name = input("Hello, what is your name?: ")
grade5 = float(input("And what is your fifth gpa?: "))
avg = (grade1+grade2+grade3+grade4+grade5)/5
print("The your average GPA is: "+str(avg))