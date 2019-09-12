import random
username=input("Hey! What's your name?")

print("Hey {}! Nice to meet you!".format(username))

favband=input("What is your favourite band dude?")

comment=["Nice, I like it.","Naah, don't like it that much.","Fair enough."]

print("Oh {}!".format(favband))

print(random.choice(comment))