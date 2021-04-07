from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-150, 270)
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Arial", 20, "normal"))

    def next_level(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!!", align="center", font=("Arial", 20, "normal"))
