from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

difficulty = {"easy": 5, "medium": 20, "hard": 50}

screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=600)
diff = screen.textinput(
    "Choose Difficulty", "Which difficulty do you want? easy, medium or hard"
)
player = Player()
level = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(cars.car_speed)
    if randint(1, 100) < difficulty[diff]:
        cars.generate_car()
    cars.move()
    for car in cars.cars:
        car_bottom = car.ycor() - 20
        car_top = car.ycor() + 20
        if player.distance(car) <= 50 and car_bottom < player.ycor() < car_top:
            game_is_on = False
            break
    if player.ycor() >= 290:
        level.next_level()
        player.refresh()
        cars.car_speed *= 0.7
    # cars.refresh()
    screen.update()

level.game_over()
screen.exitonclick()