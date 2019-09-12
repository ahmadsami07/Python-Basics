#Drawing a bar chart with turtle
#Author:Ahmad As Sami
#Date: 15th June 2019

import turtle

def drawabar(t):
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(height)
    
    return t
    

wn=turtle.Screen()
alex=turtle.Turtle()
height=100
drawabar(alex)

    