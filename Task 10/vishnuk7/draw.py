import turtle
colors = ['#e74c3c', '#8e44ad', '#2980b9', '#27ae60', '#f39c12', '#d35400']
wn=turtle.Screen()
wn.bgcolor('#34495e')
turtle.speed(0)
for x in range(70):
    turtle.pencolor(colors[x % 6])
    turtle.width(x / 100 + 4)
    turtle.forward(x*2)
    turtle.right(x/10)
    turtle.left(80)
    turtle.right(x/10)