import sys

itemsInBackpack = ["book", "computer", "keys", "travel mug"]

while True:
    print("Would you like to:")
    print("1. Add an item to the backpack?")
    print("2. Check if an item is in the backpack?")
    print("3. Quit")
    userChoice = input()

    if (userChoice == "1"):
        print("What item do you want to add to the backpack?")
        itemToAdd = input()
        itemsInBackpack.append(itemToAdd)
        print("Item '" + itemToAdd + " added to the backpack!")

    if (userChoice == "2"):
        print("What item do you want to check to see if it is in the backpack?")
        itemToCheck = input()

        if itemToCheck in itemsInBackpack:
            print("The item '" + itemToCheck + "' is in the backpack!")
        else:
            print("The item '" + itemToCheck + "' is not in the backpack!")

    if (userChoice == "3"):
        sys.exit()
