from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genarete_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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

    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Warning!", message="Website is empty!")
    elif len(email) == 0:
        messagebox.showinfo(title="Warning!", message="Email/Username is empty!")
    elif len(password) == 0:
        messagebox.showinfo(title="Warning!", message="Password is empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} "
                                                      f"\n Password: {password}"
                                                      f"\n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, 'end')
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


#logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#entry
website_entry = Entry(width=60)
website_entry.grid(column=1, row= 1, columnspan=2, sticky="nw")
website_entry.focus()

username_entry = Entry(width=60)
username_entry.grid(column=1, row= 2, columnspan=2, sticky="nw")
username_entry.insert(0, "example@emial.com")

password_entry = Entry(width=41)
password_entry.grid(column=1, row= 3, sticky="nw")

#buttons
generate_button = Button(text="Generate Password", command=genarete_pass)
generate_button.grid(column=2, row=3, sticky="nw")

add_button = Button(text="Add", width=50, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()