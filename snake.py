from turtle import Turtle
move_distance = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
START_POSITIONS = [(0, 0), (0, -20), (0, -40)]

class Snake:
    def __init__(self):
        self.segments = []
        self.new_tim()
        self.head = self.segments[0]

    def new_tim(self):
        for i in START_POSITIONS:
            self.add_segment(i)

    def add_segment(self, positions):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(positions)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

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
