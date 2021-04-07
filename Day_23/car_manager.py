from turtle import Turtle
from random import choice, randint

COLORS = ["red", "blue", "yellow", "green"]
START_SPEED = 0.1

class CarManager():
	def __init__(self):
		self.cars = []
		self.car_speed = START_SPEED
		self.generate_car()
		
	def generate_car(self):
		t = Turtle()
		t.shape("square")
		t.shapesize(stretch_wid=1, stretch_len=3)
		t.color(choice(COLORS))
		t.penup()
		t.setheading(180)
		t.goto(350, randint(-250, 250))
		self.cars.append(t)
		
	def move(self):
		for car in self.cars:
			car.forward(10)
			
	def refresh(self):
		for car in self.cars:
			car.reset()
		self.cars = []
		