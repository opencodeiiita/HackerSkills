import turtle 
wn = turtle.Screen()
wn.bgcolor("Red")
wn.title("Turtle Drawing")
loadWindow = turtle.Screen() 
turtle.speed(5) 
for i in range(10): 
    turtle.circle(5*15)  
    turtle.left(5*15) 
turtle.exitonclick() 
