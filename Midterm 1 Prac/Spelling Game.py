spell=input("Please enter a word for me to spell...")

length=len(spell)

if spell=="":
    print("Please enter a word at least!")
elif spell.isdigit():
    print("A word, not a number!")

else:
    for i in range(length):
        print("Your letter {} is {}.".format(i+1,spell[i]))

print("The word "+spell+ " has "+str(length)+" letters.")