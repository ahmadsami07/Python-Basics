#Sum Using Function
#Author:Ahmad As Sami
#Date: 18th June, 2019

def sumnum(numlist):
    sum=0
    for i in range(len(numlist)):
        sum=sum+numlist[i]
    
    print(sum)
    return sum

numberlist=[1,3,5,7,9]

sumnum(numberlist)
