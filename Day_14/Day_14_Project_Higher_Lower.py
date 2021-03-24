import csv
from random import choice, shuffle
from art import logo, vs
import os

DATA_FILE = "instagram_followers.csv"
POINTS = 0


def clear_screen():
    if os.name == "posix":
        _ = os.system("clear")
    else:
        _ = os.system("cls")


def get_data():
    """Read data from csv file and return list of dictionaries for each row"""
    data = []
    with open(DATA_FILE, "r") as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            data.append(row)
    return data


def compare(entry1, entry2):
    """Return which entry has the highest rank / most followers"""
    if entry1 < entry2:
        return "a"
    else:
        return "b"


game_data = get_data()
shuffle(game_data)

while True:
    print(logo)
    if POINTS > 0:
        print(f"Your right! Current points: {POINTS}")
    entry1 = game_data[POINTS]
    entry2 = game_data[POINTS + 1]
    print(
        f"Compare A: {entry1['owner']}, a {entry1['profession']}, from {entry1['country']}")
    print(vs)
    print(
        f"Against B: {entry2['owner']}, a {entry2['profession']}, from {entry2['country']}")
    answer = input("Who has more instagram followers? type 'a' or 'b': ")
    comparison = compare(int(entry1["rank"]), int(entry2["rank"]))
    if comparison == answer:
        POINTS += 1
        clear_screen()
    else:
        clear_screen()
        print(logo)
        print("That's wrong!")
        print(f"{entry1['owner']} has {entry1['followers']} million followers")
        print(f"{entry2['owner']} has {entry2['followers']} million followers")
        print(f"Final points: {POINTS}")
        break
