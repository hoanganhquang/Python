from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

tim = Snake()

screen.listen()
screen.onkey(tim.up, "Up")
screen.onkey(tim.down, "Down")
screen.onkey(tim.right, "Right")
screen.onkey(tim.left, "Left")

on_game = True
while on_game:
    screen.update()
    time.sleep(0.1)
    tim.move()



screen.exitonclick()

