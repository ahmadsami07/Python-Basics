#Guessing Game
#Author:Ahmad As Sami
#Date:25th May 2019
#Description: Create a game, where to win, you guess the right number.

import random
guessNumber=random.randint(1,10)
print("Doing some cheating here; the number is %d."%guessnumber)
print("Hi there! Time to play a game! Guess a number, from 1-10!")
guess=3

for i in [2, 1, 0]:
    number=input()
    if(not number.isdigit()):
        print("You are supposed to enter a number... you have entered '%s'"%number)
        #guess=guess-1
        print("You have %d guesses left."% i)
        if (guess==0):
              print("Out of guesses! Guess you couldn't win! Better luck next time!")
              break
    else:
        number=int(number)
        if (number>10):
                print("Your number was larger than 10...")
        elif(number<0):
                print("Your number is less than 0...")
        if(number==guessnumber):
                print("You got the right number mate!")
                break
        else:
            guess=guess-1
            if (guess==0):
              print("Out of guesses! Guess you couldn't win! Better luck next time!")
              break
            else:
                print("You have %d guesses left."% i)
                print("Sorry mate, try again!")   
            
    
            
        

