from turtle import Turtle


class Obj(Turtle):
    def __init__(self, xmove, ymove, _state):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(int(xmove), int(ymove))
        self.write(_state)
