import turtle, random

colors  = ["red","green","blue","orange","purple","pink","yellow"]

loadWindow = turtle.Screen() 
length=5
turtle.speed(0) 

for i in range(100): 
    color = random.choice(colors)
    turtle.forward(length)
    turtle.right(135)
    turtle.color(color)
    length = length + 5

turtle.exitonclick() 