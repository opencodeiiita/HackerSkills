
import math
import turtle

sina= turtle.Screen()

man = turtle.Turtle()
for angle in range(720):
    y = 2*math.sin(math.radians(angle)*22/28)
    man.goto(angle, y * 80)
    
    
