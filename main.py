from tkinter import *
import pandas
import random

try:
    data = pandas.read_csv("data/new.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/language.csv")

learn = data.to_dict(orient="records")
file = {}


def random_word():
    global file, flip
    window.after_cancel(flip)
    file = random.choice(learn)
    word_label.config(text=file["English"])
    title_label.config(text="English")
    flip = window.after(3000, func=meaning)


def meaning():
    try:
        title_label.config(text="Vietnamese")
        word_label.config(text=file["Vietnamese"])
    except KeyError:
        random_word()


def known():
    learn.remove(file)
    new = pandas.DataFrame(learn)
    new.to_csv("data/new.csv", index=False)
    random_word()


window = Tk()
window.title("Flashy")
window.maxsize(width=800, height=526)


flip = window.after(3000, func=meaning)


background = Canvas(width=800, height=526)
bg_image = PhotoImage(file="bg.png")
bg = background.create_image(400, 263, image=bg_image)
background.grid(row=0, column=0)

title_label = Label(text="Title", font=("Ariel", 40, "italic"), bg="white")
title_label.place(x=350, y=110)

word_label = Label(text="Word", font=("Ariel", 60, "bold"), bg="white")
word_label.place(x=330, y=225)

cancel_image = PhotoImage(file="cancel.png")
cancel_btn = Button(image=cancel_image, command=random_word)
cancel_btn.place(x=200, y=460)

check_image = PhotoImage(file="checkbtn.png")
check_btn = Button(image=check_image, command=known)
check_btn.place(x=560, y=460)

window.mainloop()
