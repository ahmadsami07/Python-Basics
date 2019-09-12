#Factorial Using Function
#Author:Ahmad As Sami
#Date: 18th June 2019

number=int(input("Please enter the number you want factorial of..."))

def factorial(n):
    fact=n
    for i in range(1,n-1):
        fact=fact*(n-i)
        
    
    print(fact)
    return fact

factorial(number)