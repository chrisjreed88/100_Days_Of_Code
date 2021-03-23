from random import randint

EASY_LIVES = 10
HARD_LIVES = 5
NUMBER = randint(1,100)

def set_difficulty():
	"""sets number of lives depending on difficulty level, easy or hard"""
	while True:
		difficulty = input("Choose difficulty, type 'easy' or 'hard': ")
		if difficulty == "easy":
			return EASY_LIVES
		elif difficulty == "hard":
			return HARD_LIVES
		else:
			print(f"{difficulty} is not valid!!")

def eval_guess(guess, lives):
	"""returns 1 less life if incorrect and prints higher or lower"""
	if guess != NUMBER:
		lives -= 1
		if lives != 0:
			print(f"Lives Remaining: {lives}")
			if guess < NUMBER:
				print("Higher!")
			else:
				print("Lower!")
		return lives
	else:
		return

def game():
	print("Welcome to the number guessing game.")
	lives = set_difficulty()
	print(f"You have {lives} tries to guess the number correctly.")
	print("I'm thinking of a number between 1 and 100.")

	guess = 0
	while guess != NUMBER and lives > 0:
		guess = int(input("Guess a number: "))
		lives = eval_guess(guess, lives)

	if lives == 0:
		print(f"The number was {NUMBER}")
		print("You lose!")
	else:
		print("That's correct!")
		print("You win!")

if __name__ == "__main__":
	game()
	
