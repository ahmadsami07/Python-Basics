#Factorial Using Recursion
#Author:Ahmad As Sami
#Date: 18th june 2019

#Description: We will figure out factorials by using recursion.

def factorial(n):
    if n<0:
        return -1
    elif n<2:
        return 1
    else:
        return n*listsum(n-1)
       
print(factorial(5))