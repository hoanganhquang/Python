from tkinter import *

PINK = "#e2979c"
RED = "#e7385b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = Tk()
window.title("Pomodoro")
window.config(padx=40, pady=50, bg=GREEN)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=662, height=377, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="png-clipart-computer-icons-scalable-graphics-tomato-emoji-food-tomato-removebg-preview.png")
canvas.create_image(331, 188.5, image=tomato_img)
canvas.create_text(331, 215, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(row=1, column=1)

tick = Canvas(width=50, height=50, highlightthickness=0, bg=GREEN)
tick.create_text(25, 25, text="✔", fill="white", font=(FONT_NAME, 30, "bold"))
tick.grid(row=3, column=1)

start_btn = Button(text="Start")
start_btn.config(padx=20)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset")
reset_btn.config(padx=20)
reset_btn.grid(row=2, column=2)

window.mainloop()

