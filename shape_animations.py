import turtle
from time import sleep
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animation Shapes")

t = turtle.Turtle()
t.color("red")
t.speed(0)
t.hideturtle()
t.pensize(5)

# growing circle
for i in range(100):
    t.circle(i*2)
    t.lt(5)

t.clear()

# collapsing circle
t.lt(500)
for i in range(100, 1, -1):
    t.circle(i*2)
    t.rt(5)

t.clear()

# growing triangle
for i in range(50):
    t.lt(120)
    t.forward(i*10)


sleep(2)