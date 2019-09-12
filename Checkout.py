#Making A Supermarket Sales Program
#Author:Ahmad As Sami
#Date: 15th June,2019

def checkout():
    total=0
    count=0
    moreitems=True
    while moreitems:
        price=int(input("What is the price of the item?(enter 0 if finished)"))
        if price<0:
            print("Error. Please enter again:")
        else:
            if price!=0:
                    total=total+price
                    count=count+1
            else:
                moreitems=False
    print("Your bill is {}, and you bought {} item(s) today.".format(total,count))

checkout()