from turtle import Turtle

MOVE = 10
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270


class Snake:
    def __init__(self):
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        self.snakes = [Turtle("square") for _ in range(3)]
        for snake in range(len(self.snakes)):
            self.snakes[snake].color("white")
            self.snakes[snake].penup()
            self.snakes[snake].speed("fastest")
            self.snakes[snake].goto(0 - snake * 20, 0)

    def move(self):
        for snake in range(len(self.snakes) - 1, 0, -1):
            self.snakes[snake].showturtle()
            new_x = self.snakes[snake - 1].xcor()
            new_y = self.snakes[snake - 1].ycor()
            self.snakes[snake].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.speed("fastest")
        new_snake.hideturtle()
        self.snakes.append(new_snake)

    def hit_wall(self):
        x = self.head.xcor()
        y = self.head.ycor()
        if x <= -290 or x >= 290:
            return True
        elif y <= -290 or y >= 290:
            return True
        else:
            return False

    def hit_self(self):
        collision = False
        for snake in self.snakes[3:]:
            if self.head.distance(snake) <= 20:
                collision = True
        return collision
