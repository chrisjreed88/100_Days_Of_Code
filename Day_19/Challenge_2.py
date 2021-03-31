import turtle
from random import randint

s = turtle.Screen()
s.setup(500, 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = [turtle.Turtle(shape="turtle") for color in colors]


def goto_start():
    for n, turtle in enumerate(turtles):
        y = -100 + (n + 1) * 30
        turtle.color(colors[n])
        turtle.penup()
        turtle.goto(-200, y)


def race():
    winner = False
    finish_line = 225
    while not winner:
        for turtle in turtles:
            turtle.forward(randint(0, 10))
            if turtle.xcor() >= finish_line:
                winner = turtle.pencolor()
    return winner


goto_start()
user_bet = s.textinput(
    title="Bet on who will win",
    prompt="Type the color of the turtle that you think will win.",
)
winner = race()
print(f"{winner} won!")
if user_bet.lower() == winner:
    print("You won the bet!")
else:
    print("You lost!")

s.exitonclick()