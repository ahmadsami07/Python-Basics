#String Format Method

person=input("Your name:")
greeting="Hello {}!".format(person)
print(greeting)


#Calculation

origprice=float(input("Please Enter The Original Price= "))
discount=float(input("Enter discount percentage="))
newprice=origprice-(discount/100)*100
calculation="${:0.2f} was the original price, after {}% discount, price is ${:0.2f}.".format(origprice,discount,newprice)
print(calculation)