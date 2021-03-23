from random import choice
import os
from ascii_cards import *
from art import logo

def clear_screen():
	if os.name == "posix":
		_ = os.system("clear")
	else:
		os.system("cls")
		
def get_score(cards):
	score = sum([card.points for card in cards])
	if score > 21:
		for n, card in enumerate(cards):
			if card.points == 11:
				cards[n].points = 1
				score = sum([card.points for card in cards])
				break
	return score

def deal_cards(num_cards):
	cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
	suits = ["diamonds", "spades", "hearts", "clubs"]
	dealt_cards = [Card(choice(suits), choice(cards)) for n in range(num_cards)]
	return dealt_cards
				
def game():
	player_cards = deal_cards(2)
	player_score = get_score(player_cards)
	computer_cards = deal_cards(2)
	computer_score = get_score(computer_cards)
	blackjack = True if player_score == 21 else False
	dealer_blackjack = True if computer_score == 21 else False
	while player_score < 21:
		print(f"Your hand:")
		print(ascii_version_of_card(*player_cards))
		print(f"Total: {player_score}\n")
		print(f"Computers hand:")
		print(ascii_version_of_hidden_card(*computer_cards))
		while True:
			draw = input("Type 'y' to twist or 'n' to stick: ").lower()
			if not draw in ["y", "n"]:
				print(f"{draw} is not a valid response!")
			else:
				break
		if draw == "y":
			player_cards.extend(deal_cards(1))
			player_score = get_score(player_cards)
		else:
			break
	if not blackjack:
		while computer_score < 17:
			computer_cards.extend(deal_cards(1))
			computer_score = get_score(computer_cards)
	print(f"Your final hand:")
	print(ascii_version_of_card(*player_cards))
	print(f"Computer final hand:")
	print(ascii_version_of_card(*computer_cards))
	print(f"Player Score: {player_score}")
	print(f"Computer Score: {computer_score}")
	if dealer_blackjack:
		print("Dealer got blackjack! You lose!")
	elif blackjack:
		print("BLACKJACK! You win")
	elif player_score > 21:
		print("You went over 21. You lose!")
	elif computer_score > 21:
		print("Dealer went over 21. You win!")
	elif player_score == computer_score:
			print("It's a draw!")
	elif player_score > computer_score:
			print("You win!")
	else:
			print("You lose!")

while input("Do you want to play a game of blackjack? y or n: ") == "y":
	clear_screen()
	print(logo)
	game()