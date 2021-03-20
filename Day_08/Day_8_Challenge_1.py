import math

def paint_calc(height, width, cover):
	num_cans = math.ceil(height * width / cover)
	print(f"You will need {num_cans} cans of paint.")
	

height = int(input("What is the height of the wall? "))
width = int(input("What is the width of thw wall? "))
cover = 5
paint_calc(height=height, width=width, cover=cover)