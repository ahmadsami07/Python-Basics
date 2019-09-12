#Predicting Chatbot

name=input("Please enter your name:")
age=int(input("please, enter your age:"))

charlength=len(name)
count=0
for i in range(charlength):
    if name[i]=='E' or name[i]=='e':
        count=count+1

newage=age+13

print("There are " +str(count)+ " letter(s) 'e' or 'E' in your name.")
print("In 13 years you will be be "+str(newage)+ " years old.")
print('Bye!')