from turtle import Screen, Turtle
from game_logic import Game

game = Game()
turtle = Turtle()
turtle.hideturtle()
turtle.penup()
screen = Screen()
screen.setup(height=491, width=725)
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")

game_is_on = True
while game_is_on:
    guess = screen.textinput(
        title=f"{game.score}/50 states correct", prompt="Guess a State")
    state_coords = game.take_guess(guess)
    if state_coords:
        turtle.goto(state_coords)
        turtle.write(guess)
    else:
        game_is_on = False

screen.exitonclick()
