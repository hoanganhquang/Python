from tkinter import *
from tkinter import messagebox
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
               , 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'
               , 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def ran_pass():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list1 = [random.choice(letters) for letter in range(nr_letters)]
    password_list2 = [random.choice(numbers) for letter in range(nr_numbers)]
    password_list3 = [random.choice(symbols) for letter in range(nr_symbols)]

    password_list = password_list1 + password_list2 + password_list3
    random.shuffle(password_list)

    password = "".join(password_list)

    input_pass.insert(0, password)
    pyperclip.copy(password)


def save_info():
    if len(input_website.get()) < 1 or len(input_email.get()) < 1 or len(input_pass.get()) < 1:
        messagebox.showwarning(title="Oops", message="Data invalid")
    else:
        ok = messagebox.askokcancel(title=input_website.get(), message=f"Email: {input_email.get()}\n "
                                                                       f"Password: {input_pass.get()}\n "
                                                                       f"Are you sure?")
        if ok:
            with open("info.txt", "a") as file:
                file.write(f"{input_website.get()} | {input_email.get()} | {input_pass.get()}\n")

            input_website.delete(0, END)
            input_email.delete(0, END)
            input_pass.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file="pass.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website", font=("Times", 10))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=("Times", 10))
email_label.grid(row=2, column=0)

pass_label = Label(text="Password", font=("Times", 10))
pass_label.grid(row=3, column=0)

input_website = Entry(width=51)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()

input_email = Entry(width=51)
input_email.grid(row=2, column=1, columnspan=2)

input_pass = Entry(width=33)
input_pass.grid(row=3, column=1)

generate = Button(text="Generate Password", command=ran_pass)
generate.grid(row=3, column=2)

add_btn = Button(text="Add", width=42, command=save_info)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
