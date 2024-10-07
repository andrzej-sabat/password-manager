import json
from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genarete_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password

        }}
    if len(website) == 0:
        messagebox.showinfo(title="Warning!", message="Website is empty!")
    elif len(email) == 0:
        messagebox.showinfo(title="Warning!", message="Email/Username is empty!")
    elif len(password) == 0:
        messagebox.showinfo(title="Warning!", message="Password is empty!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- SEARCHING ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if website in data:
                record = data[website]
                messagebox.showinfo(title=f"Searching: {website}",
                                    message=f"Email: {record["email"]}\n"
                                            f"Password: {record["password"]}")
            else:
                messagebox.showwarning(title="Error", message="Website not found.")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data file not found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, padx=10, pady=10)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2, padx=10, pady=10)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, padx=10, pady=10)

# entry
website_entry = Entry(width=41)
website_entry.grid(column=1, row=1, sticky="nw", padx=10, pady=15)
website_entry.focus()

username_entry = Entry(width=64)
username_entry.grid(column=1, row=2, columnspan=2, sticky="nw", padx=10, pady=15)
username_entry.insert(0, "example@emial.com")

password_entry = Entry(width=41)
password_entry.grid(column=1, row=3, sticky="nw", padx=10, pady=15)

# buttons
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1, sticky="nw", padx=10, pady=10)

generate_button = Button(text="Generate Password", width=15, command=genarete_pass)
generate_button.grid(column=2, row=3, sticky="nw", padx=10, pady=10)

add_button = Button(text="Add", width=51, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, padx=10, pady=10)

window.mainloop()
