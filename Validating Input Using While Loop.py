#Validating Input
#Ahmad As Sami
#Date:15th June 19
#Description: We will create a function which validates input only to 'Y' (yes)or 'N' (no)

def validation():
    valid=True
    while valid:
        response=input("So, do you like lentil soup? Y/N")
        response=response.lower()
        if response=="y" or response=="n":
            valid=False
        else:
            print("Please enter a 'Y' or 'N' response!")

    return response

answer=validation()
if answer =="Y"or answer=="y" :
    print("Great! I absolutely love it!")
else:
    print("Hmm...creep.")