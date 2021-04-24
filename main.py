from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="W", fun=l_paddle.up)
screen.onkey(key="S", fun=l_paddle.down)

on_game = True
while on_game:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor() == 270:
        ball.wall()









screen.exitonclick()

