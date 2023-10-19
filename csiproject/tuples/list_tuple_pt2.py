# More List/Tuples
name = "CSI-160: Introduction to Python Programming"
title = name.find("Python")
count = name.count("Python")
slice = name[title:]
space = slice.find(" ")
new_name = slice[0:space]


def splicing():
    print(title)
    print(count)
    print(slice)
    print(space)
    print(new_name)


# splicing()


letters = ['a', 'w', 'q', 'z', 'd', 's', 'w', 's', 'w']
letters_tuple = tuple(letters)
# print(letters)
# print(letters_tuple)
# .count() and .find() dont work on lists
'''
pos = letters.find('a')
count = letters.count('a')
'''


# IN CLASS ACTIVITY

def find_letter(string, toLook):
    count_letter = 0
    str_pos = ""
    for pos in range(len(string)):
        if string[pos] == toLook:
            count_letter += 1
            str_pos += str(pos) + ", "
        else:
            continue
    str_pos = str_pos[0:-2]
    if count_letter > 0:
        print("The value '" + toLook + "' was found ", count_letter, " times at index(es)", str_pos)
    elif count_letter == 0:
        print("The value '" + toLook + "' was not found!")
    else:
        print("There was an error in this function: please try again")


find_letter(name, "z")
