# CTI-100
# M5LAB3 Snowflake
# Michael Hathaway
# 16 October 2017

#  ********NOTE********
#  Pleae go FULL SCREEN

import turtle
import random
wn = turtle.Screen()
t = turtle.Turtle()
t.pensize(5)
wn.bgcolor("gray")
# Snowflake 1: standard snowflake rendered in cyan
def branch():
    for i in range(3):
        for i in range (3):
            t.forward(30)
            t.backward(30)
            t.right(45)
        t.left(90)
        t.backward(30)
        t.left(45)
    t.right(90)
    t.forward(90)
for i in range(8):
    t.color("cyan")
    branch()
    t.left(45)
# Snowflake 2: Hexagon surrounded by 6 Octagons rendered in red
t.penup()
t.forward(250)
t.left(0)
t.pendown()
t.pensize(2)
t.pencolor("red")
for i in range(6):
    t.left(60)
    t.forward(50)
    for i in range(8):
        t.forward(20)
        for i in range(9):
            t.forward(10)
            t.backward(10)
            t.right(45)

# Snowflake 3: 12-sideed polygon rendereed in white
t.penup()
t.right(120)
t.forward(150)
t.pendown()
t.pensize(1)
t.pencolor("white")



def branch():
    for i in range(1):
        t.forward(100)
        for i in range (2):
            t.backward(50)
            for i in range(2):
                t.right(30)
                t.forward(30)
                t.backward(30)
            t.left(90)
            t.forward(30)
            t.backward(30)
            for i in range(15):
                t.right(30)
                t.forward(30)
                t.backward(30)
            
for i in range (12):
    branch()
    t.right(270)




wn.exitonclick()
