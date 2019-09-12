#Summation Program With A WHile Loop
#Author: Ahmad As Sami
#Date: 15th June 2019
#Desciption: Create a sum of n numbers, whitch gives the sum of all numbers upto it.

def sumto(n):
    anumber=1
    sumnumber=0
    while anumber<=n:
        sumnumber=sumnumber+anumber
        anumber=anumber+1
    return sumnumber    



limitnumber=int(input("Upto which number do you want the sum?"))

print(sumto(limitnumber))
