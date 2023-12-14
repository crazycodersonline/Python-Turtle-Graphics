import turtle
from time import sleep


t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-300,-300)
t.pendown()


size = 75
count = 1
isblack = True

def square(t):
    t.begin_fill()
    t.setheading(90)
    t.forward(size)
    t.setheading(0)
    t.forward(size)
    t.setheading(270)
    t.forward(size)
    t.setheading(180)
    t.forward(size)
    t.end_fill()
    t.setheading(90)

def switch_color(t):
    global isblack
    if isblack:
        t.fillcolor("black")
        isblack = False
    else:
        t.fillcolor("white")
        isblack = True
    

for i in range(1,65):
    switch_color(t)

    square(t)    

    t.penup()

    if i % 8 == 0:
        t.goto(-300+(size*count) ,-300)
        switch_color(t)
        count += 1

    else:
        t.forward(size)
    t.pendown()
    

sleep(3)
