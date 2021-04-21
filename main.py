import turtle
from turtle import  Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Choose color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    race = True

while race:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race=False
            win = turtle.pencolor()
            if win == user_bet:
                print("You win")
            else:
                print("you lost")
        ran_distance = random.randint(0, 10)
        turtle.forward(ran_distance)



screen.exitonclick()

