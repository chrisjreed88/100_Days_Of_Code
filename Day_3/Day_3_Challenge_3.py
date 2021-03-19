year = int(input("Enter the year: "))

if year % 4 == 0:
	if year % 100 == 0 and not year % 400 == 0:
		print(f"The year {year} is not a leap year")
	elif year % 100 == 0 and year % 400 == 0:
		print(f"The year {year} is a leap year")
	else:
		print(f"The year {year} is a leap year")
else:
	print(f"The year {year} is not a leap year")
		
			