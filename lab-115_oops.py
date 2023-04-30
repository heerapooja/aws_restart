#Exercise 1: Working with a while loop
import random

#printing the game rules
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

num = random.randint(1,10)
gs = False #is guess right variable
while gs!=True:
    gs=input("Guess a number between 1 and 10: ")
    if int(gs)==num:
        print("you gussed {}. That is correc! You win!".format(gs))
        gs=True
    else:
        print("You guessed {}. Sorry, that isn't is. Try again.".format(gs))

#Informing the user about the script
print("Count to 10!")

#Writing the for loop
for x in range(0,11):
    print(x)
