from turtle import Turtle
from random import choice

START_HEADINGS_R = [n for n in range(10, 80, 10)]
START_HEADINGS_R.extend([n for n in range(280, 350, 10)])
START_HEADINGS_L = [n for n in range(100, 260, 10)]
HEADINGS = [START_HEADINGS_L, START_HEADINGS_R]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.refresh()
        self.ball_speed = 0.05

    def refresh(self, side=False):
        if side == "right":
            self.direction = choice(START_HEADINGS_L)
        elif side == "left":
            self.direction = choice(START_HEADINGS_R)
        else:
            direction = choice(HEADINGS)
            self.direction = choice(direction)
        self.setheading(self.direction)
        self.goto(0, 0)
        self.ball_speed = 0.05

    def move(self, player_paddle, computer_paddle):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.reflect_off_wall()
        elif self.detect_hit(player_paddle) or self.detect_hit(computer_paddle):
            self.reflect_off_paddle()
        else:
            self.forward(10)

    def detect_hit(self, paddle):
        hit = False
        if paddle.xcor() < 0:
            if self.distance(paddle) <= 50 and self.xcor() <= -265:
                hit = True
        else:
            if self.distance(paddle) <= 50 and self.xcor() >= 265:
                hit = True
        return hit

    def reflect_off_wall(self):
        new_direction = 360 - self.direction
        self.setheading(new_direction)
        self.direction = new_direction
        self.forward(20)

    def reflect_off_paddle(self):
        new_direction = 180 - self.direction
        self.setheading(new_direction)
        self.direction = new_direction
        self.forward(20)
        self.ball_speed *= 0.9
