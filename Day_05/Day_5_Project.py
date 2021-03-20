from random import choice, randint

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letters.extend([l.upper() for l in letters])
numbers = [str(n) for n in range(10)]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator\n")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = ""
for letter in range(nr_letters):
	password += choice(letters)

for symbol in range(nr_symbols):
	password += choice(symbols)

for number in range(nr_numbers):
	password += choice(numbers)

randomized_password = ""
for char in range(len(password)):
	random_index = randint(0, len(password) - 1)
	random_char = password[random_index]
	password = password[:random_index] + password[random_index+1:]
	randomized_password += random_char
	
print(f"\nPassword: {randomized_password}")

"""
Solution in video:
	
make password variable a list using method as above

use random.shuffle() function to randomize the password list

join back together as string using for loop
"""
