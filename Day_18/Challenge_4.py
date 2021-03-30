from turtle import Turtle, Screen, colormode
from random import choice, randint

t = Turtle()
s = Screen()
colormode(255)
t.pensize(10)
t.speed(0)


def random_color():
    red = randint(1, 255)
    green = randint(1, 255)
    blue = randint(1, 255)
    return (red, green, blue)


directions = [0, 90, 180, 270]

for _ in range(500):
    t.color(random_color())
    t.forward(15)
    t.setheading(choice(directions))

s.exitonclick()
