from tkinter import *
import pandas as pd
from pandas import errors
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
except errors.EmptyDataError:
    df = pd.read_csv("data/french_words.csv")
column1 = str(df.columns.values[0])
column2 = str(df.columns.values[1])
data = df.to_dict(orient="records")


def next_card():
    if len(data) == 0:
        completed()
    else:
        global current_card, flip_timer
        window.after_cancel(flip_timer)
        current_card = choice(data)
        canvas.itemconfig(card, image=card_front_image)
        canvas.itemconfig(title_text, text=column1, fill="black")
        canvas.itemconfig(word_text, text=current_card[column1], fill="black")
        flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card, image=card_back_image)
    canvas.itemconfig(title_text, text=column2, fill="white")
    canvas.itemconfig(word_text, text=current_card[column2], fill="white")


def remove_card():
    try:
        data.remove(current_card)
        remaining_cards.config(text=f"Cards Remaining: {len(data)}")
    except ValueError:
        pass
    df = pd.DataFrame(data)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def completed():
    canvas.itemconfig(card, image=card_back_image)
    canvas.itemconfig(title_text, text="Well Done!!", fill="white")
    canvas.itemconfig(word_text, text="You've Completed\n       The Deck", fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)


card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
wrong_button_image = PhotoImage(file="images/wrong.png")
right_button_image = PhotoImage(file="images/right.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(column=0, row=1, columnspan=2)

wrong_button = Button(
    image=wrong_button_image, borderwidth=0, highlightthickness=0, command=next_card
)
wrong_button.grid(column=0, row=2)
right_button = Button(
    image=right_button_image, borderwidth=0, highlightthickness=0, command=remove_card
)
right_button.grid(column=1, row=2)

remaining_cards = Label(
    text=f"Cards Remaining: {len(data)}", bg=BACKGROUND_COLOR, fg="white"
)
remaining_cards.grid(column=0, row=0, columnspan=2)

next_card()

window.mainloop()
