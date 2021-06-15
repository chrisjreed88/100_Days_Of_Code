from tkinter import *
from tkinter.messagebox import askokcancel, askquestion, showerror, showinfo, showwarning
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letters.extend([l.upper() for l in letters])
    numbers = [str(n) for n in range(10)]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    password = [choice(letters) for letter in range(randint(8, 10))]
    password.extend([choice(symbols) for symbol in range(randint(2, 4))])
    password.extend([choice(numbers) for number in range(randint(2, 4))])
    shuffle(password)
    new_password = "".join(password)
    password_entry.delete(0, END)
    password_entry.insert(END, string=new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) < 1 or len(password) < 1:
        showwarning(
            title="Oops", message="Please don't leave any fields blank!")
    else:
        new_data = {
            website: {
                "email": email,
                "password": password
            }
        }
        if askokcancel(title=website, message=f"Details to be saved:\n\nEmail: {email}\nPassword: {password}\n\nIs this correct?"):
            exists = False
            changed = False
            try:
                with open("password_data.json", "r") as f:
                    data = json.load(f)
                    if website in data:
                        exists = True
            except FileNotFoundError:
                data = new_data
            else:
                if exists:
                    if askquestion(title="Exists", message=f"An entry for {website} already exists,\nDo you want to replace it?") == "yes":
                        data[website]["password"] = password
                        changed = True
                else:
                    data.update(new_data)
            finally:
                with open("password_data.json", "w") as f:
                    json.dump(data, f, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                if changed:
                    showinfo(title="Changed",
                             message="Your password has been changed!")
                else:
                    showinfo(title="Saved",
                             message="Your password has been saved!")


# ---------------------------- SEARCH DATABASE ------------------------------- #

def search():
    website = website_entry.get()
    if len(website) > 0:
        with open("password_data.json", "r") as f:
            data = json.load(f)
        try:
            email = data[website]["email"]
            password = data[website]["password"]
        except KeyError:
            message = f"Entry for {website} not found!"
        else:
            message = f"Email: {data[website]['email']}\nPassword: {data[website]['password']}"
            pyperclip.copy(password)
        finally:
            showinfo(title=website, message=message)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# window.geometry("500x400")
window.config(padx=50, pady=50, bg="white")

logo = PhotoImage(file="logo.png")

# Canvas for logo
canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
canvas.create_image(100, 100, image=logo)

# Labels
website_label = Label(text="Website:", bg="white", pady=3)
email_label = Label(text="Email / Username:   ", bg="white", pady=3)
password_label = Label(text="Password:", bg="white", pady=3)

# Entries
website_entry = Entry()
website_entry.focus()
email_entry = Entry()
email_entry.insert(END, string="example@hotmail.com")
password_entry = Entry()

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", command=save_data)
search_button = Button(text="Search", command=search)

# Add to grid
canvas.grid(column=1, row=0)
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
website_entry.grid(column=1, row=1, sticky="ew")
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
password_entry.grid(column=1, row=3, sticky="ew")
generate_button.grid(column=2, row=3, sticky="ew")
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")
search_button.grid(column=2, row=1, sticky="ew")


window.mainloop()
