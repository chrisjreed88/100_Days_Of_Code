print("Welcome to the love calculator!\n")

name1 = input("What is your name?\n").lower()
name2 = input("What us their name?\n").lower()
names = name1 + name2

"""
This is how I would do it

love = 0
true = 0

for char in "true":
	num_times = names.count(char)
	true += num_times
for char in "love":
	num_times = names.count(char)
	love += num_times
"""

# For loops not taught yet so this is how it
# was demonstrated

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")
true = t + r + u + e

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")
love = l + o + v + e

score = int(str(true) + str(love))
if score < 10 or score > 90:
	print(f"Your score is {score}, you go together like coke and mentos!")
elif 40 <= score <= 50:
	print(f"Your score is {score}, you go alright together")
else:
	print(f"Your score is {score}")
	