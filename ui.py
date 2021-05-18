from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.canvas.create_text(150, 125, text="Text", fill=THEME_COLOR)

        self.true_btn = Button(text="True")
        self.true_btn.grid(row=2, column=0)

        self.false_btn = Button(text="False")
        self.false_btn.grid(row=2, column=1)

        self.window.mainloop()
