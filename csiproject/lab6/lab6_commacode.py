listToPrint = []
while True:
    newWord = input("Enter a word to add to the list (press return to stop adding words): ")
    if newWord == "":
        break
    else:
        listToPrint.append(newWord)

stringToPrint = ""
for i in range(len(listToPrint)):
    if i == len(listToPrint) - 1:  # If the element is the last element
        stringToPrint += 'and ' + listToPrint[i]  # Append to the string the word 'and' and the element
    else:
        stringToPrint += listToPrint[i] + ', '  # If not the last element, just add a comma

print(stringToPrint)
