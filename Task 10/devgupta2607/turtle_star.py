import turtle
wn= turtle.Screen()
wn.bgcolor("black")
wn.title("star")
skk= turtle.Turtle()
skk.color("yellow")

skk.begin_fill()
for i in range(5):
    skk.forward(50)
    skk.right(144)
skk.end_fill()

turtle.done()   
