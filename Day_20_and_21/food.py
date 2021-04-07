from turtle import Turtle
from random import randint, choice

FOOD_COLOURS = ["blue", "orange", "purple", "red"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        self.color(choice(FOOD_COLOURS))
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)
