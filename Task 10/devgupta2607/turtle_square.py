import turtle
wn= turtle.Screen()
wn.bgcolor("light green")
wn.title("square")
skk= turtle.Turtle()
skk.color("red")

skk.begin_fill()
for i in range(4):
    skk.forward(100)
    skk.right(90)
skk.end_fill()

turtle.done()   
