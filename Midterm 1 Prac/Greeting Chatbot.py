#Greeting Chatbot
# Say Hi!, what's your name? and get the user's name
# The string "Hi!, what's your name? " is called a prompt
username = input("Hi!, what's your name? ")

# Respond Nice to meet you, <username>
print("Nice to meet you, " + username)

# Chatbot asks you what is your favourite music band
favBand = input("Hey " + username + ", what is your favourite music band? ")

# Make a comment
print("Oh!{}! I like this band!".format(favBand))

