from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 265)
        self.write_scoreboard()

    def write_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_scoreboard()

    def final_score(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over!!\n", align=ALIGNMENT, font=FONT)
        self.write_scoreboard()
