#Nosy Bot
#Description: Create a chatbot, which will ask at least 3 questions.
#Author: Ahmad As Sami
#Date: 15th May 2019

#Ask for the name of the user, then respond that the name is nice.
username=input("Hi there! What's your name? ")
print("Hmmm..."+username+ ", that's a nice name!")

#Ask for the user's major.
major=input("So...what is your major? ")
#If it is computing science, chatbot will respond it is the favourite field, while for business, it will ask for selling it a pen.
if major=="Computing Science":
  print("Hey " +major+ "! That, in fact, is also my favourite field of study!\n")
elif major=="Business":
  print("So...here is a pen. Try selling it to me!\n")
#If the response is something else, the chatbot will simply give a generic response(quite interesting).
else:
  print("Hmm... that's quite interesting!\n")  
  


#The chatbot will now ask for the user's favourite coffee shop.
favcafe=input("So moving on...Tim Horton's or Starbucks!? ")
#For Starbucks, will respond that the chatbot loves starbucks, and if response is Tim Horton's, the chatbot will suggest the user to try it out.
if favcafe=="Starbucks":
  print("A classy choice! I love Starbucks!\n")
elif favcafe=="Tim Horton's":
  print("Really? You better try out Starbucks!\n")
#If the user doesn't reply of the either, the chatbot will just say it never heard of it.
else:
  print("Never heard of that.\n")

#The chatbot will ask for the user's favourite burger joint.
favburger=input("And your favourite burger joint? \n")
#For McDonald's response, chatbot will tell the user to check out a new meal.
if favburger=="McDonald's":
  print("There's a new meal in, check it out!\n")
#For KFC, the chatbot will imply that one of the burgers its is favourite.
elif favburger=="KFC":
  print("The Hot Zinger is simply my favourite!\n")
#For any other joint, the chatbot will simply respond that's nice.
else:
  print("That's nice!\n")

#A concluding statement from the chatbot.
print("So that's it for today! Hope I didn't bore you to death already!")