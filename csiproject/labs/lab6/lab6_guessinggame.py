# Guessing game with infinite guesses
from random import randint

randomNum = randint(1, 100)  # Generate random number

guess = -1

while guess != randomNum:  # While the guess is incorrect
    guess = int(input("Guess a whole number between 1 and 100:"))  # Get a new guess (assumes int)
    if guess == randomNum:  # If the guess is correct
        print("That's right!")
        break
    elif guess > randomNum:  # If the correct answer is less than the guess
        print("Nope! It is less than that!")
    else:
        print("Nope! It is greater than that!")  # If the correct answer isn't less than
        # or equal to the guess, it is greater
