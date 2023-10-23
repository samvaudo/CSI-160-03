# A program to play a guessing game between the numbers 0 and 9 with the user
from random import randint

random_num = randint(0, 9)  # randomizing number

guess = int(input("Guess a whole number between 0 and 9:"))  # getting guess

if guess == random_num:  # determining if the number guessed was the random number
    print("You are correct!")
else:
    print("Incorrect! The number was ", random_num)
