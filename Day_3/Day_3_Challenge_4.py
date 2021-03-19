print("Welcome to the pizza deliveries!\n")

size = input("What size pizza do you want? s, m, l: ")
add_pepperoni = input("Do you want pepperoni? y or n: ")
extra_cheese = input("Do you want extra cheese? y or n: ")

if size == "s":
	bill = 15
	if add_pepperoni == "y":
		bill += 2
elif size == "m":
	bill = 20
	if add_pepperoni == "y":
		bill += 3
else:
	bill = 25
	if add_pepperoni == "y":
		bill += 3
	
if extra_cheese == "y":
	bill += 1

print(f"Your total bill is ${bill}")