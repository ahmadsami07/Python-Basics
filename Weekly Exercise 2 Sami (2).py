#How's it going? Chatbot-version 4
#Description: Write a chatbot that asks a user how their day is going
#and make a comment that changes depending on how the user answered
#Author: Ahmad As Sami
#Date: 15h May 2019

#Say How is it going? and get user's reply
reply=input("How is it going?")

#Say glad to hear if the user is doing well
if reply == "Awesome!"or reply=="Great" or reply=="Well!":
    print("Glad to hear!")
elif reply=="Great!":
    print("Glad to hear!")
#Say sorry to hear things are not going well!
elif reply==("Bad!"):
    print("Sorry to hear things are not going well!") 
else:
#A generic comment which works in most situations
    print("Oh I see...")    