#Guessing Game

import random

randomnumb=random.randint(1,10)
print(str(randomnumb))
guesses=3

for guess in range (0,3):
    guessnumb=guesses-1-guess
    usergues=("Please enter your guess!")
    print("You have {}  guesses remaining...".format(guessnumb))
    
    if usergues.isalpha():
        print("Please enter a number...")
    else:
        usergues=int(usergues)
        if(usergues>10)or(userguss<10):
            print("Please enter a number between 0 and 10.")
        else:
            if usergues==randomnumb:
                print("You got it!")
    if guessnumb==0:
        break