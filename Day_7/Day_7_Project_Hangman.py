import requests
from random import choice
import os

def clear_screen():
	if os.name == "posix":
		_ = os.system("clear")

def hidden_word():
	hidden = ""
	for char in word:
		if char in correct_guesses:
			hidden += char + " "
		else:
			hidden += "_ "
	return hidden

def get_random_word(word_length):	
	word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
	response = requests.request("GET", word_site)
	words = response.content.splitlines()
	word = choice(words).decode("ASCII")
	while len(word) != word_length:
		word = choice(words).decode("ASCII")
	return word

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print("""
_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                      
""")
word_length = int(input("How many letters do you want the word to have? "))

word = get_random_word(word_length)
#print("the word is " + word)
correct_guesses = []
incorrect_guesses = []
lives = 6
while len(correct_guesses) != len(word):
	print(hidden_word())
	guess = input("\nGuess a letter: ")
	if guess in word:
	   for n in range(word.count(guess)):
	   	correct_guesses.append(guess)
	else:
		if not guess in incorrect_guesses:
			clear_screen()
			print(stages[lives])
			incorrect_guesses.append(guess)
			if lives == 0:
				print(f"The word was {word}")
				print("You Lose!")
				break
			lives -= 1
		else:
			print(f"You already guessed {guess}")

if len(correct_guesses) == len(word):
	print(hidden_word())
	print("You Win!")