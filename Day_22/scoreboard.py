from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, screen_side):
        super().__init__()
        self.side = screen_side
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        if self.side == "left":
            x = -150
        else:
            x = 150
        self.goto(x, 260)
        self.write_score()

    def write_score(self):
        self.write(self.score, align="center", font=("Arial", 24, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()
