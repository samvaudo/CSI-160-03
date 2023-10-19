#Working with conditionals and loops

mixedList = ["john", "sally", "sam", "Larry", "Mary", 1, 2, 6, 7, "sam", 9, 8, 2, 4, 5]
title = "Python programming"
emptyList = []

def searchList():
    '''
    searches the whole list for the entry 'sam' and counts each time
    :return: printing the time 'sam' was found in the list above
    '''
    count = 0
    for i in mixedList:
        if i == "sam":
            count+=1
        else:
            pass
    print("The entry 'sam' was found",count,"time(s) in the list")


searchList()