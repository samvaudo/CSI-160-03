# Guessing game with infinite guesses
from random import randint

randomNum = randint(1,100)

guess = -1

while guess != randomNum:
    guess = int(input("Guess a whole number between 1 and 100:"))
    if guess == randomNum:
        print("Thats right!")
        break
    elif guess > randomNum:
        print("Nope! It is less than that!")
    else:
        print("Nope! It is greater than that!")
