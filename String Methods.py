#String Methods
#Author: Ahmad As Sami
#Date: 19th May 2019
#Description: Working with different string methods

ss="Hello World"
print(ss.upper())
print(ss.lower())

qp="Goodbye World"

tt=(qp.lower())
print(tt)

print(ss.count("1"))

print("***" + ss.strip() + "***")
print("***" + ss.lstrip() + "***")
print("***" + ss.rstrip() + "***")

news=ss.replace("o","*")
print(news)


food="banana bread"
print("***"+food.capitalize()+"***")
print("***"+food.center(25)+"***")
print("***"+food.ljust(25)+"***")
print("***"+food.rjust(25)+"***")

print(food.find("e"))
print(food.find("na"))
print(food.find("b"))