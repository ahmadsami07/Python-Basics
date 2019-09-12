#Spelling Bot
#Author:Ahmad As Sami
#Date: 27th May
#Description: A program which can spell out each word.

spell=input("Please enter the word you want to spell.").replace(" ","")

spellist=list(spell)

strlen=int(len(spellist))

for index in range(strlen):
    print("Letter '"+str(index+1) +"' is "+str(spellist[index]))

print("The word " +spell+ " has " +str(strlen)+ " letters.")