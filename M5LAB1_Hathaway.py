#CTI-110
# M5LAB1 Shapes
# Hathaway, Michael
# 16 October 2017


import turtle
win = turtle.Screen()
t = turtle.Turtle()

# Set display
t.pensize(5)
t.pencolor("red")
t.shape("turtle")

# Square
for i in range(4):
  t.forward(100)
  t.right(90)

# Move the pen
t.penup()
t.backward(50)
t.pendown()

# Set new display
t.pensize(3)
t.pencolor("blue")
t.shape("arrow")

# Triangle
for i in range(3):
    t.forward(200)
    t.left(120)

# Move the pen
t.penup()
t.forward(100)
t.pendown()

# Set new display
t.pensize(7)
t.pencolor("green")
t.shape("turtle")

# Circle
for i in range(360):
    t.forward(2)
    t.right(1)

  
    
