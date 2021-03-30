from turtle import Turtle, Screen, colormode
from random import choice
from colors import colors

t = Turtle()
s = Screen()
t.pensize(10)
colormode(255)


def draw_row():
    for _ in range(10):
        t.color(choice(colors))
        t.dot()
        t.forward(50)


t.penup()
for n in range(-200, 200, 40):
    t.goto(-250, n)
    draw_row()

s.exitonclick()
