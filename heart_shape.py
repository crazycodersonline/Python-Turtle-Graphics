import turtle
from time import sleep

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(450,350)
t.color("red")
t.penup()
t.setpos(0,-130)
t.pendown()
t.begin_fill()

t.fillcolor('red')
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(180)

t.end_fill()

sleep(1)
