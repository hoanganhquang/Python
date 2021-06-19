from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, input_required, Length
import pandas


class CafeForm(FlaskForm):
    cafe_name = StringField("Cafe name", validators=[DataRequired()])
    cafe_location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired()])
    open_time = StringField("Opening Time e.g.8AM", validators=[DataRequired()])
    close_time = StringField("Closing Time e.g.5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=[(1,"✘"),(2,"☕"), (3,"☕☕"), (4,"☕☕☕"), (5,"☕☕☕☕"), (6,"☕☕☕☕☕")])
    wifi = SelectField("Wifi Strength Rating", choices=[(1,"✘"),(2,"💪"), (3,"💪💪"), (4,"💪💪💪"), (5,"💪💪💪💪"), (6,"💪💪💪💪💪")])
    power_socket = SelectField("Power Socket Availability",  choices=[(1,"✘"),(2,"🔌"), (3,"🔌🔌"), (4,"🔌🔌🔌"), (5,"🔌🔌🔌🔌"), (6,"🔌🔌🔌🔌🔌")])



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


@app.route('/add', methods=["POST", "GET"])
def add_page():
    cafe_form = CafeForm()
    cafe_form.validate_on_submit()
    if cafe_form.validate_on_submit():
        with open("cafe-data.csv", mode="a") as file:
            file.write(f"\n{cafe_form.cafe_name.data},{cafe_form.cafe_location.data},{cafe_form.open_time.data},{cafe_form.close_time.data},{cafe_form.coffee_rating.data},{cafe_form.wifi.data},{cafe_form.power_socket.data}")

    return render_template('add.html', form=cafe_form)


if __name__ == "__main__":
    app.run(debug="on")
