from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.refresh()

    def move_forward(self):
        self.forward(20)

    def refresh(self):
        self.goto(0, -280)
