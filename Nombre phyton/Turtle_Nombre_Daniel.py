import turtle

t = turtle.Turtle()

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

# Fondo de círculos coloridos
for i in range(6):
    for colors in ["purple", "aqua", "magenta", "green", "lime", "white"]:
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(10)

turtle.speed(10)
turtle.pensize(10)

# Dibujo del nombre "DANIEL"
t = turtle.Turtle()
t.speed(3)
t.shape("square")
t.pensize(35)

# D
t.color("aqua")
t.penup()
t.goto(-500, -90)
t.pendown()
t.left(90)
t.forward(140)
t.right(90)
t.circle(-70, 180)

# A
t.color("lime")
t.penup()
t.goto(-330, -90)
t.setheading(75)
t.pendown()
t.forward(150)
t.right(130)
t.forward(150)
t.penup()
t.left(160)
t.forward(40)
t.left(85)
t.forward(15)
t.pendown()
t.forward(90)

# N
t.color("magenta")
t.penup()
t.goto(-160, -90)
t.setheading(90)
t.pendown()
t.forward(140)
t.right(145)
t.forward(170)
t.left(145)
t.forward(140)

# I
t.color("blue")
t.penup()
t.goto(20, -90)
t.setheading(90)
t.pendown()
t.forward(140)

# E 
t.color("orange")
t.penup()
t.goto(120, 50)
t.setheading(270)  
t.pendown()
t.forward(140)    

t.penup()
t.goto(120, 50)
t.setheading(0)
t.pendown()
t.forward(70)


t.penup()
t.goto(120, -20)
t.setheading(0)
t.pendown()
t.forward(50)

t.penup()
t.goto(120, -90)
t.setheading(0)
t.pendown()
t.forward(70)


# L
t.color("yellow")
t.penup()
t.goto(270, 50)
t.setheading(270)
t.pendown()
t.forward(140)
t.left(90)
t.forward(90)

turtle.done()