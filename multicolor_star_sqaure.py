import turtle
from time import sleep

tp = turtle.Turtle()
screen = turtle.Screen()
screen.setup(450,350)
screen.bgcolor('black')
colors = ['red', 'green', 'blue', 'yellow', 'purple']
tp.pensize(10)
tp.setpos(-90,30)

# multicolor star
for i in range(5):
    tp.pencolor(colors[i])
    tp.forward(160)
    tp.right(144)

tp.clear()

# multicolor sqaure
for i in range(4):
    tp.pencolor(colors[i])
    tp.forward(100)
    tp.right(90)

sleep(2)
