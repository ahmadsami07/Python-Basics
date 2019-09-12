#Greetings Chatbot Version 3

# Description: Write a chatbot that can say Hi! and learn your name
# Author: Ahmad As Sami
# Date: May 10, 2019
import random
# Say Hi!, what's your name? 
# print("Hi!, what's your name?")

# Get the user's name
# The string "Hi!, what's your name? " is the argument to the function "input( )"
# The string "Hi!, what's your name? " is called a prompt
username = input("Hi!, what's your name? ")
#Create a list of random comments
comments=["Oh! I like this band.","Hum...are they still performing?","OhOh!I don't enjoy them."]
# Respond Nice to meet you, <username>
print("Nice to meet you, " + username)
#Say what is your favourite music band?
band=input("So, what is your favourite band?")
#Make a response based on that.
print(random.choice(comments))