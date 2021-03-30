from turtle import Turtle, Screen
from random import choice

t = Turtle()
s = Screen()

colours = ["red", "green", "yellow", "blue"]

for shape in range(3, 11):
	t.color(choice(colours))
	angle = 360 / shape
	for side in range(shape):
		t.forward(100)
		t.right(angle)
		
s.exitonclick()
	