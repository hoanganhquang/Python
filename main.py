from flask import Flask
import random

app = Flask(__name__)
random_num = random.randint(0, 9)


@app.route('/')
def home_page():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp'>"


@app.route('/<number>')
def guess(number):
    number = int(number)
    if number > random_num:
        return "<h1>Too high, try again!</h1>"
    elif number < random_num:
        return "<h1>Too low, try again!</h1>"
    else:
        return "<h1>You found me!</h1>"


if __name__ == "__main__":
    app.run(debug="on")
