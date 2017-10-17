# CTI-110
# M5LAB2 Initials
# Hathaway, Michael
# 16 October 2017
import turtle          

win = turtle.Screen()  
t = turtle.Turtle()

# Display options
t.pensize(7)        # Pen Size
t.pencolor("blue")  # Pen Color
t.shape("arrow")    # Pointer Type

# draw the box letter M
t.left(180)
t.forward(100)
t.left(72)
t.forward(60)
t.right(144)
t.forward(60)
t.left(72)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(60)
t.left(90)
t.forward(120)
t.right(150)
t.forward(60)
t.left(60)
t.forward(60)
t.left(60)
t.forward(60)
t.right(150)
t.forward(120)
t.left(90)
t.forward(60)
t.left(90)
t.forward(200)
t.right(90)
# Lift the pen and move it to the next letter
t.penup()
t.forward(75)
t.pendown()
# Draw the box letter H
t.right(90)
t.forward(200)
t.left(90)
t.forward(50)
t.left(90)
t.forward(75)
t.right(90)
t.forward(50)
t.right(90)
t.forward(75)
t.left(90)
t.forward(50)
t.left(90)
t.forward(200)
t.left(90)
t.forward(50)
t.left(90)
t.forward(75)
t.right(90)
t.forward(50)
t.right(90)
t.forward(75)
t.left(90)
t.forward(50)
# end command
win.mainloop()
# Wait for user to close window
