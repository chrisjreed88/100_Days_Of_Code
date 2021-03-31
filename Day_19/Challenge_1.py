import turtle

t = turtle.Turtle()
s = turtle.Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def move_left():
    t.left(10)


def move_right():
    t.right(10)


def clear():
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.pendown()


turtle.listen()
turtle.onkey(key="w", fun=move_forward)
turtle.onkey(key="s", fun=move_backward)
turtle.onkey(key="a", fun=move_left)
turtle.onkey(key="d", fun=move_right)
turtle.onkey(key="c", fun=clear)

s.exitonclick()