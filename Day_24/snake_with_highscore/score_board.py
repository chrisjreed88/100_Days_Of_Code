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
        with open("highscore.txt") as f:
            self.highscore = int(f.read())
        self.new_highscore = False
        self.write_scoreboard()

    def write_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}, Highscore: {self.highscore}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore += 1
            self.new_highscore = True
        self.write_scoreboard()

    def final_score(self):
        self.goto(0, 0)
        self.write("Game Over!!\n", align=ALIGNMENT, font=FONT)
        if self.new_highscore:
            with open("highscore.txt", "w") as f:
                f.write(str(self.highscore))
            self.write(f"\nNew Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)
