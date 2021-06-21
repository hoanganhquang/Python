from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class EditForm(FlaskForm):
    your_rating = StringField("Your Rating Out of 10 e.g 7.5", validators=[DataRequired()])
    your_review = StringField("Your Review", validators=[DataRequired()])


class Movie(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    title = db.Column(db.VARCHAR(100), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.VARCHAR(1000), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.VARCHAR(500), nullable=False)
    img_url = db.Column(db.VARCHAR(1000), nullable=False)


db.create_all()


@app.route("/")
def home():
    data_movie = db.session.query(Movie).all()
    return render_template("index.html", data=data_movie)


@app.route("/edit<int:id_movie>", methods=["POST", "GET"])
def edit(id_movie):
    form = EditForm()
    if form.validate_on_submit():
        get_movie = Movie.query.get(id_movie)
        get_movie.rating = float(form.your_rating.data)
        get_movie.review = form.your_review.data
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit.html", form=form, id_send=id_movie)


if __name__ == '__main__':
    app.run(debug=True)
