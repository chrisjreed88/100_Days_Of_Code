from turtle import Turtle, Screen
from random import choice

t = Turtle()
s = Screen()
t.pensize(10)
t.speed(0)

directions = [0, 90, 180, 270]
colors = ["cyan", "spring green", "dark salmon",
          "orange", "dark khaki", "dark slate grey"]


for _ in range(500):
    t.color(choice(colors))
    t.forward(15)
    t.setheading(choice(directions))

s.exitonclick()
