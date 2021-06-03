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

while game.score < 50:
    try:
        guess = screen.textinput(
            title=f"{game.score}/50 states correct", prompt="Guess a State").title()
    except AttributeError:
        continue
    if guess == "Exit":
        game.generate_states_to_learn_csv()
        break
    state_coords = game.take_guess(guess)
    if state_coords:
        turtle.goto(state_coords)
        turtle.write(guess)
