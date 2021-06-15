import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in df.iterrows()}


def generate_nato():
    word = input("Enter a word: ").upper()
    try:
        nato_word = [nato_dict[char] for char in word]
    except KeyError:
        print("Sorry, only letters please")
        generate_nato()
    else:
        print(nato_word)


generate_nato()
