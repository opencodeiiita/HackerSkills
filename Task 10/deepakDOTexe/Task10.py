import tkinter
import turtle
import math

car=turtle.Turtle()
car.color("#F7F7F7")
car.pensize(10)

ts = turtle.getscreen()
car.getscreen().bgcolor("#444444")
car.left(90)
car.penup()
car.forward(100)
car.pendown()
car.right(90)
# car.begin_fill()
car.forward(200)
car.right(180)
car.forward(400)
car.left(60)
car.forward(141.4214)
car.right(60)
car.forward(100)
car.left(90)
car.forward(100)
car.left(90)
car.forward(150)
car.right(90)
car.circle(75)
car.left(90)
car.penup()
car.forward(150)
car.pendown()
car.forward(200)
car.right(90)
car.circle(75)
car.left(90)
car.penup()
car.forward(150)
car.pendown()
car.forward(150)
car.left(90)
car.forward(100)
car.left(90)
car.forward(100)
car.right(45)
car.forward(180)
# car.left(45)
# car.end_fill()


ts.getcanvas().postscript(file="car2.jpg")
turtle.done()