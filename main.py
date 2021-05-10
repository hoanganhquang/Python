from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7385b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
BREAK_MIN = 5
reps = 0
timer = None


def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg="white")
    canvas.itemconfig(timer_text, text=f"00:00")
    check_mark.config(text="")
    reps = 0


def start_timer():
    global reps
    reps += 1
    work = WORK_MIN * 60
    short_break = BREAK_MIN * 60

    if reps % 2 == 0:
        countdown(short_break)
        timer_label.config(text="Break", fg="white")
        window.deiconify()
    else:
        countdown(work)
        timer_label.config(text="Work", fg="white")


def countdown(count):

    _min = math.floor(count / 60)
    _sec = count % 60
    if _min < 10:
        _min = f"0{_min}"
    if _sec < 10:
        _sec = f"0{_sec}"

    canvas.itemconfig(timer_text, text=f"{_min}:{_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)

        if len(mark) == int(input_.get()):
            window.after_cancel(timer)
            reset_timer()
            check_mark.config(text=mark)


window = Tk()
window.title("Pomodoro")
window.config(bg=GREEN, padx=30)
window.maxsize(730, 500)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg="white", bg=GREEN)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=662, height=377, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="png-clipart-computer-icons-scalable-graphics-tomato-emoji-food-tomato-removebg-preview.png")
canvas.create_image(331, 188.5, image=tomato_img)
timer_text = canvas.create_text(331, 215, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(row=1, column=1)

type_label = Label(text="Enter quantity", font=(FONT_NAME, 11, "bold"), fg="white", bg=GREEN)
type_label.place(x=5, y=5)

input_ = Entry(width=5)
input_.place(x=137, y=6)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer, font=(FONT_NAME, 12, "bold"))
start_btn.config(padx=20, pady=10)
start_btn.place(x=50, y=400)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer, font=(FONT_NAME, 12, "bold"))
reset_btn.config(padx=20, pady=10)
reset_btn.place(x=510, y=400)

check_mark = Label(font=(FONT_NAME, 30), fg="white", bg=GREEN)
check_mark.grid(row=2, column=1)

window.mainloop()

