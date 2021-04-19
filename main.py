import turtle
from turtle import Turtle, Screen
import random

color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]
turtle.colormode(255)

tur = Turtle()
tur.shape("circle")
tur.setheading(225)
tur.forward(300)
tur.setheading(0)
num = 100


for i in range(1, num):
    tur.dot(20, random.choice(color_list))
    tur.penup()
    tur.forward(50)

    if i % 10 == 0:
        tur.setheading(98)
        tur.forward(50)
        tur.setheading(180)
        tur.forward(500)
        tur.setheading(0)



screen = Screen()
screen.exitonclick()
