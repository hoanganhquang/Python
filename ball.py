from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto(newx, newy)

    def bounce(self):
        self.ymove *= -1

    def b_paddle(self):
        self.xmove *= -1
        self.move_speed *= 0.9

    def game_reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.b_paddle()



