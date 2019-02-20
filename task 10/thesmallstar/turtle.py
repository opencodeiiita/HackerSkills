import turtle
a = turtle.Turtle()
a.speed(-1000)
sz = 2 
for i in range(500):
    a.right(100)
    a.forward(sz)
    sz = sz+0.5
