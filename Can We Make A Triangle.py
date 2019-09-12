#Can We Make A Triangle?
#Author:Ahmad As Sami
#Date:30th June 2019

def istriangle(a,b,c):
  if (a>b+c) or (b>a+c) or (c>a+b):
    return False
  else:
    return True

  
def Triangle():
  num1=int(input("Inputting the lengths..."))
  num2=int(input("Inputting the lengths..."))
  num3=int(input("Inputting the lengths..."))
  if istriangle(num1,num2,num3):
    print("Yes")
  else:
    print("No.")
  

Triangle()