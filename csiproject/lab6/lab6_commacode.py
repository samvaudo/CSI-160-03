listToPrint = []
while True:
    newWord = input("Enter a word to add to the list (press return to stop adding words): ")
    if newWord == "":
        break
    else:
        listToPrint.append(newWord)


stringToPrint = ""
for i in range(len(listToPrint)):
    if i == len(listToPrint) - 1:
        stringToPrint += 'and ' + listToPrint[i]
    else:
        stringToPrint += listToPrint[i]  + ', '



print(stringToPrint)