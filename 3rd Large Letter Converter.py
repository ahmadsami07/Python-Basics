#3rd Letter Large Converter
#Author: Ahmad As Sami
#Date: 30th June 2019

test=input("")

length=len(test)
reform=""
for i in range (length):
  if i%3==0:
    reform=reform+(test[i]).capitalize()
  else:
    reform=reform+test[i]


print(reform)