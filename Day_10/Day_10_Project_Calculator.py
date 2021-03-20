import os
from art import logo
import sys

def clear_screen():
	if os.name == "posix":
		_ = os.system("clear")
	else:
		_ = os.system("cls")

def add(n1, n2):
	return n1 + n2
	
def subtract(n1, n2):
	return n1 - n2
	
def multiply(n1, n2):
	return n1 * n2
	
def divide(n1, n2):
	return n1 / n2

def calc():
	operations = {
		"+": add, 
		"-": subtract, 
		"*": multiply, 
		"/": divide
		}
	try:
		clear_screen()
		print(logo)
		print("Press Ctrl + C at anytime to exit the calculator")
		num1 = int(input("What is the first number?\n"))

		finished = False
		while not finished:
			for operation in operations:
				print(operation)
			operation = input("What operation do you want to use?\n")
			num2 = int(input("What is the next number?\n"))

			func = operations[operation]
			result = func(num1, num2)

			print(f"{num1} {operation} {num2} = {result}")
			cont = input(f"Type 'y' to perform another operation on {result}, or 'n' to start again: ").lower()
			if cont == "n":
				finished = True
				calc()
			else:
				num1 = result
	except KeyboardInterrupt:
		sys.exit(0)

if __name__ == "__main__":			
	calc()