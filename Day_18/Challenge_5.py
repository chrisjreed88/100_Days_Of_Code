from turtle import Turtle, Screen, colormode
from random import choice, randint

t = Turtle()
s = Screen()
colormode(255)
t.pensize(2)
t.speed(0)


def random_color():
    red = randint(1, 255)
    green = randint(1, 255)
    blue = randint(1, 255)
    return (red, green, blue)


angle = 5
for _ in range(int(360 / angle)):
    t.color(random_color())
    t.circle(radius=100)
    t.left(angle)

s.exitonclick()
