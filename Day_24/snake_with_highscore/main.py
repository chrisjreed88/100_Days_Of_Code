from snake import Snake
from turtle import Screen
from food import Food
from time import sleep
from score_board import ScoreBoard

screen = Screen()
food = Food()
score = ScoreBoard()
snake = Snake()

screen.setup(600, 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake")

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while not snake.hit_wall() and not snake.hit_self():
    sleep(0.03)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        score.increase_score()
    screen.update()

score.final_score()
screen.exitonclick()