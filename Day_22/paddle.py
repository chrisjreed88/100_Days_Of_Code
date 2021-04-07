from turtle import Turtle
from random import choice

START_POSITIONS = [-40, -20, 0, 20, 40]
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)
        self.setheading(UP)

    def go_up(self):
        self.setheading(UP)
        if self.ycor() <= 250:
            self.forward(20)

    def go_down(self):
        self.setheading(DOWN)
        if self.ycor() >= -250:
            self.forward(20)
