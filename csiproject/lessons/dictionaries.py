# An intro to dictionaries

example = {'key': 'value'}

courses = {'CSI-160': 'Intro to Python', 'CSI-260': 'Adv. Python', 'CSI-300': 'Database Systems'}

# del courses
# print(courses)

courses.update({'CSI-261': 'Advanced Python Programming'})  # This updates the value based on its key.
courses.update({'CSI-2601': 'Advanced Python Programming'})
# If it is not in the dictionary, it adds it!
# print("updated dictionary:", courses)
'''
courses['CSI-400'] = 'Software Engineering'  # Adds a new item to the dictionary
print('adding an item to a dictionary:', courses)

courses['CSI-260'] = 'Adv. Python Prog.'  # Performs the update if the key already exists
print("adding/updating an item to a dictionary:", courses)

del courses['CSI-260']
print("deleted an item in a dictionary:", courses)
'''

# Preserving data from a dictionary - it can be added back after a delete
# key = input("Enter a key to delete:")
key = 'CSI-260'
value = courses.pop(key)  # The key notation tells the interpreter to pass a value to the variable
print(key, value)
print("Deleted a key in a dictionary:", courses)

courses[key] = value
print("Added back deleted item in dictionary:", courses)

print("Sorted Dictionary:", dict(sorted(courses.items())))  # Sorts for keys in memory, but it is not a permanent sort
print("Unsorted Dictionary:", courses)  # Prints dictionary as is, not sorted

print("Sorted by values Dictionary:",dict(sorted(courses.items(), key=lambda item: item[1])))  # Sorts on the values in memory, but it is not a permanent sort

0
