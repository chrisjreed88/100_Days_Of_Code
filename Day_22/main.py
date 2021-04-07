from turtle import Screen
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(600, 600)
screen.tracer(0)
l_score = ScoreBoard(screen_side="left")
r_score = ScoreBoard(screen_side="right")
l_paddle = Paddle((-280, 0))
r_paddle = Paddle((280, 0))
ball = Ball()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

while True:
    time.sleep(ball.ball_speed)
    if ball.xcor() >= 290:
        l_score.update_score()
        ball.refresh(side="right")
    elif ball.xcor() <= -290:
        r_score.update_score()
        ball.refresh(side="left")
    else:
        ball.move(l_paddle, r_paddle)
    screen.update()

screen.exitonclick()
