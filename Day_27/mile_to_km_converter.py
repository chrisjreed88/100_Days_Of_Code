from tkinter import *


def calculate():
    if len(box.get()) >= 1:
        miles_integer = int(box.get())
        kilometres = round(miles_integer * 1.609, 2)
        answer.config(text=str(kilometres))
    else:
        answer.config(text="0")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=20)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

box = Entry(width=10)
box.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

answer = Label(text="0")
answer.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

button = Button(text="calulate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
