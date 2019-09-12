#Predicting Chatbot
#Author: Ahmad As Sami
#Description: Asks our name and agge , how many characters of E, and how many characters in our name.
#First take inputs for name and age
name=input("Please, enter your name:")
age=input("Please, enter your age:")
#Next, we find length of the input i.e. name.

length=len(name)

#Then we use a for loop, to find out how many 'e' and 'E' there are, we take a variable, count.

count=0
for i in range(length):
    if(name[i]=='e' or name[i]=='E'):
        count=count+1
#Now, we display input.
print("Dear {}:".format(name))
print("Your name has" +str(length)+"characters.")
print("There are"+str(count)+"'E' and or 'e' in your name.")

print("Bye!")