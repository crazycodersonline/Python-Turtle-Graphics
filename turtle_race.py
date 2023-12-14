import turtle
import random
from time import sleep

t = turtle.Turtle()

t.penup()
t.goto(280, 200)
style = ("Courier", 20, 'bold')
t.write("Finish Line", font=style, align='center')
t.pendown()
t.goto(280, -200)
t.penup()
t.goto(-200, 100)

t.shape('turtle')
t.color("purple")
t2 = t.clone()
t2.penup()
t2.goto(-200, -100)
t2.color("orange")

dice = [1, 2, 3, 4, 5, 6]
while True:
    die_outcome = random.choice(dice)
    print(f"\nPlayer 1 die outcome {die_outcome}")
    t.fd(die_outcome)

    if t.pos() >= (280, 100):
        message = "Player 1 Wins"
        break

    die_outcome = random.choice(dice)
    print(f"\nPlayer 2 die outcome {die_outcome}")
    t2.fd(die_outcome)

    if t2.pos() >= (280, -100):
        message = "Player 2 Wins"
        break

sleep(1)
t2.hideturtle()
t.color("red")
t.goto(0, 0)
style = ("Courier", 20, 'bold')
t.write(message, font=style, align='center')



sleep(2)