import tkinter

# Create window

window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

# Label

label = tkinter.Label(text="My Label", font=("Arial", 24, "bold"))
# label.pack(side="left")
label.grid(column=0, row=0)

# changing values

label["text"] = "My New Label"
label.config(text="My New Label")

# Button


def button_clicked():
    label.config(text=entry.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry

entry = tkinter.Entry(width=10)
entry.grid(column=3, row=2)


window.mainloop()
