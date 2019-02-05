import turtle
import random
a = turtle.Turtle()
while True:
  a.speed(-1000)
  sz = 2 
  ang = random.randint(1, 302)
  for i in range(500):
    a.right(ang)
    a.forward(sz)
    sz = sz+0.5
  a.clear()
  a.reset()
