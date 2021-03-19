from random import randint

#scores = [78,65,89,86,55,91,64,89]
scores = [randint(50,100) for n in range(10)]

heighest_score = 0
for score in scores:
	if score > heighest_score:
		heighest_score = score

print(f"The heighest score is {heighest_score}")