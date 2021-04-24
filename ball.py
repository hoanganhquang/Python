from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()

    def move(self):
        newx = self.xcor() + 10
        newy = self.ycor() + 10
        self.goto(newx, newy)

    def change(self):
        newx = self.xcor() - 10
        newy = self.ycor() + 10
        self.goto(newx, newy)

    def wall(self):
        newx = self.xcor() + 10
        newy = self.ycor() - 10
        self.goto(newx, newy)
