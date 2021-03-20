import os
from art import logo

def clear_screen():
	if os.name == "posix":
		_ = os.system("clear")
	else:
		_ = os.system("cls")

def add_bid():
	name = input("What is your name?\n")
	amount = int(input("Enter bid amount: $"))
	bid = {"name":name, "amount":amount}
	bids.append(bid)
	
def find_highest_bidder(bids):
	highest_bid = 0
	highest_bidder = ""
	for bid in bids:
		if bid["amount"] > highest_bid:
			highest_bidder = bid["name"]
			highest_bid = bid["amount"]
	print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

bids = []	
print(logo)
add_bidders = True
while add_bidders:
	add_bid()
	if input("Are there any more bidders? yes or no: ") == "no":
		add_bidders = False
	clear_screen()
	
find_highest_bidder(bids)