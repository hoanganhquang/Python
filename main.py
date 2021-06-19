from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
import pandas


class CafeForm(FlaskForm):
    cafe_name = StringField("Cafe name")
    cafe_location = StringField("Cafe Location on Google Maps (URL)")
    open_time = StringField("Opening Time e.g.8AM")
    close_time = StringField("Closing Time e.g.5:30PM")
    coffee_rating = SelectField("Coffee Rating")
    wifi = StringField("Wifi Strength Rating")
    power_socket = StringField("Power Socket Availability")



app = Flask(__name__)
Bootstrap(app)
app.secret_key = "key"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cafes')
def cafes_page():
    file = pandas.read_csv('cafe-data.csv')
    file_dict = file.to_dict().items()
    file1 = file.iterrows()
    return render_template('cafes.html', data=file_dict, data1=file1)


@app.route('/add')
def add_page():
    cafe_form = CafeForm()
    return render_template('add.html', form=cafe_form)


if __name__ == "__main__":
    app.run(debug="on")
