#More about dictionaries

courses = {'CSI-160':'Intro to Python', 'CSI-260':'Adv. Python', 'CSI-300':'Database Systems'}

#del courses
#print(courses)

courses.update({'CSI-261':'Advanced Python Programming'}) #This updates a value based on its key
courses.update({'CSI-2601':'Advanced Python Programming'})
#print('Updated dictionary:',courses)
"""
courses['CSI-400'] = 'Software Engineering' #Adds a new item to the dictionary
print(courses)

courses['CSI-260'] = 'Adv. Python Prog.' #Performs the update if the key already exists
print('Adding an item to a dictionary:',courses)

del courses['CSI-260']
print(courses)


#Preserving data from a dictionary - it can be added back after a delete
key = input("Enter a key to delete:")
value = courses.pop(key) #The key notation tells the interperter to pass the value to the variable
#print(key , value)
#print(courses)

courses[key] = value

print(courses)

dict(sorted(courses.items())) #Sorts on the keys in memory but it is not a permanent sort
print("Sorted dictionary:",courses) #Outputs the dictionary as it is, not sorted

print(dict(sorted(courses.items(), key=lambda item: item[1] ))) #Sorts on the values in memory but it is not a permanent sort
#print(courses)
"""
def thisProcess():
    count = 0
    v = ''
    k = input("Enter the key:")
    for keys, values in courses.items():
        if keys == k:
            v = values
            count += 1
        else:
            continue
    if count > 0:
        print("the value associated with the key",k,"equals:",v)
    elif count == 0:
        add = input("Key not found. Do you want to add the key, value pairing? (y/n)")
        if add == 'y':
            v = input("Enter a course name:")
            courses[k] = v
            print(courses)
    else:
        print("Process failed")

thisProcess()