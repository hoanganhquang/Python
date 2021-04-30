import turtle
import pandas
from obj import Obj

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

file = pandas.read_csv("50_states.csv")
data = file.state
true_answer = 0
exist_obj = []
remain = []

on_game = True
while on_game:
    answer_state = screen.textinput(title=f"{true_answer}/50 States Correct", prompt="What's another state's name?")
    if answer_state == "exit":
        break
    else:
        for _state in data:
            if answer_state == _state.lower() and answer_state not in exist_obj:
                true_answer += 1
                data1 = file[file.state == _state]
                obj = Obj(data1.x, data1.y, _state)
                exist_obj.append(_state)
            if true_answer == 50:
                break


for answer in data:
    if answer not in exist_obj:
        remain.append(answer)

pandas.DataFrame(remain).to_csv("states_to_learn.csv")


