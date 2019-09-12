#Fortune Cookie Bot
#Description:Write a chatbot which can tell your fortune!
#Author: Ahmad As Sami
#Date: 13th May 2019
import random

#Say Hi, What's your name?
print("Hi, what's your name?")

username=input()

#Create a list of fortunes
comments=["You shall die in 5 hours, 15 minutes, 23 seconds from now.","Drink a glass of water or you shall die from poisoning.","You shall live for 103 years."]
print(random.choice(comments))