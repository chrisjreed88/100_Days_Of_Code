from random import randint

moves = ["rock", "paper", "scissors"]

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

drawings = [rock, paper, scissors]
while True:
	try:
		player_input = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors:\n"))
		if 0 <= player_input <=2:
			break
		else:
			print("Invalid number!!")
	except ValueError:
		print("You must use the numbers provided!!")
	
player_choice = moves[player_input]
computer_input = randint(0, 2)
computer_choice = moves[computer_input]

print("You chose:")
print(drawings[int(player_input)])
print("Computer chose:")
print(drawings[int(computer_input)])


if player_choice == computer_choice:
	print("It's a draw")
elif player_choice == "rock" and computer_choice == "paper":
	print("You lose")
elif player_choice == "paper" and computer_choice == "scissors":
	print("You lose")
elif player_choice == "scissors" and computer_choice == "rock":
	print("You lose")
else:
	print("You win")