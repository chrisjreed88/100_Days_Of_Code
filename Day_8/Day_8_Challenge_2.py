def prime_checker(number):
	n = number - 1
	while n >= 1:
		if n == 1:
			print(f"{number} is prime")
			n = 0
		elif number % n == 0:
			print(f"{number} is not prime")
			n = 0
		else:
			n -= 1
	"""
	# Solution in video:
	is_prime = True
	for i in range(2, number):
			if number % i == 0:
				is_prime = False
	print(f"{number} is prime = {is_prime}")
	
	# This is probably better :(
	"""
			
number = int(input("Enter a number: "))
prime_checker(number)