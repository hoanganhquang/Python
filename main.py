from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)



@app.route('/')
def home_page():
    data_posts = requests.get(url="https://api.npoint.io/9d1c9613b0bbd767e135")
    data = data_posts.json()
    return render_template('index.html', response=data)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact_page():
    message = False
    if request.method == 'POST':

        message = True

    return render_template('contact.html', message=message)


@app.route('/post<int:num>')
def to_post(num):
    data_posts = requests.get(url="https://api.npoint.io/9d1c9613b0bbd767e135")
    data = data_posts.json()
    return render_template('post.html', post=data, num=num)


if __name__ == "__main__":
    app.run(debug="on")
