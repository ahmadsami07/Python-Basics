#Cumulative Sum
#Author:Ahmad As Sami
#Date:2nd July 2019

t=[1,2,3]
length=len(t)
print(length)
def cumsum(a):
    sum=0
    for i in range(length):
        sum=sum+a[i]
    print(sum)
    return cumsum
cumsum(t)
