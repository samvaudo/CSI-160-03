"""DESCRIPTION OF THE MODULE GOES HERE
Author:Sam Vaudo
Class:CSI-160-03
Assignment: Week 2: Lab - Conversation with a Computer
Due Date: 9/15

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""
#setting variables
name = ""
age = 0
siblings = 0
food = ""
sib_shares_food_response = ""
sib_shares_food_bool = False
sib_shares_food = "No"
parents_age = 0
gpa1 = 0
gpa2 = 0


#asking for name
name = input("Hello, what is your name?\n")

#asking for age
age = int(input("Hello "+name+", how old are you?\n"))

#asking for number of siblings
siblings = int(input("And how many siblings do you have, "+name+"?\n"))

if siblings < 0:#not allowing negative siblings
    siblings = 0

#asking for favorite food
food = input("What is your favorite food, "+name+"?\n")

#statement to not ask about sibling's favorite food if there are no siblings
if siblings>0:

    #getting a response for if a sibling shares a favorite food
    sib_shares_food_response = input("Ok, you are one of "+str(siblings+1)+" kids. Does any of your "+str(siblings)+" sibling(s) have the favorite food of "+food+"? (y/n)\n")

    #turning the response into a boolean
    sib_shares_food_bool = sib_shares_food_response == "y"

    #setting the text value from boolean for final result
    if sib_shares_food_bool:
        sib_shares_food = "Yes"

else:
    #setting sharing food varialbe to N/A if question wasn't asked
    sib_shares_food = "N/A"

#asking parent's age
parents_age = int(input("And how old are your parents, "+name+"?\n"))

#asking for first and second gpa
gpa1 = float(input("Ok, and one final set of questions, what is your first semester GPA?\n"))
gpa2 = float(input("And the second semester GPA?\n"))

#calculating average
avg = (gpa1+gpa2)/2


#printing results
print("Your results:\nName: "+name+"\nAge: "+str(age)+"\n# of siblings: "+str(siblings)+"\nFavorite Food: "+food+"\nDo(es) your sibling(s) share your favorite food? "+sib_shares_food+"\nAge of parents: "+str(parents_age)+"\nAverage GPA: "+str(avg))