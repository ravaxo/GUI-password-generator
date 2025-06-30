from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# List of characters for generating password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    """Generates a random secure password and displays it in the password entry field."""
    letter_count = random.randint(5,8)
    number_count = random.randint(5,8)
    symbol_count = random.randint(5,8)

    letter_list = [random.choice(letters) for _ in range(letter_count)]
    number_list = [random.choice(numbers) for _ in range(number_count)]
    symbol_list = [random.choice(symbols) for _ in range(symbol_count)]

    pre_password = letter_list + number_list + symbol_list
    random.shuffle(pre_password)

    password = "".join(pre_password)

    text_password.delete(0, END)
    text_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def data():
    """Saves the website, email, and password to a text file after user confirmation."""
    website = text_website.get()
    email = text_email_username.get() 
    password = text_password.get()

    if len(website) and len(email) and len(password) != 0:
        ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}"
                                        f"\nPassword: {password}\nIs it okay to save?")
        if ok:
            with open("details.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
                text_website.delete(0,'end')
                text_password.delete(0,'end')
    else:
        messagebox.showinfo(title="oops", message="Please don't keep any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
# Initializes the main GUI window and layout

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email_username = Label(text="Email/Username:")
label_email_username.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# Text Entry
text_website = Entry(width=55)
text_website.grid(column=1, row=1, columnspan=2)
text_website.focus()

text_email_username = Entry(width=55)
text_email_username.grid(column=1, row=2, columnspan=2)
text_email_username.insert(0, "example@email.com")

text_password = Entry(width=36)
text_password.grid(column=1, row=3)

# Buttons
button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=47, command=data)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
