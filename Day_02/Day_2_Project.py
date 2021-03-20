print("Welcome to the tip calculator.")
while True:
    try:
        total = float(input("What was the total bill? £"))
        tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
        people = int(input("How many people to split the bill? "))
        amount = (total * (1 + (tip / 100))) / people
        print(f"Each person should pay: £{'{:.2f}'.format(amount)}")
        break
    except ValueError:
        print("You need to enter a number!!")

