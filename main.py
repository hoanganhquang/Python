from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

tim = Snake()
food = Food()
score = Score()

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
    if tim.head.distance(food) < 15:
        food.refresh()
        score.total_score()
        tim.extend()
    if tim.head.xcor() > 280 or tim.head.xcor() < -280 or tim.head.ycor() > 280 or tim.head.ycor() < -280:
        score.game_over()
        on_game = False
    for s in tim.segments[1:]:
        if tim.head.distance(s) < 10:
            on_game = False
            score.game_over()
screen.exitonclick()

