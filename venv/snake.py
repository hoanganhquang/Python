from turtle import Turtle
move_distance = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.new_tim()
        self.head = self.segments[0]

    def new_tim(self):
        x = 0
        for i in range(0, 3):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x, 0)
            x -= 20
            self.segments.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
