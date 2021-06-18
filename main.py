from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import pandas

file = pandas.read_csv('cafe-data.csv')
print(file.iloc[[0]])


# app = Flask(__name__)
# Bootstrap(app)
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
#
# @app.route('/cafes')
# def cafes_page():
#     file = pandas.read_csv('cafe-data.csv', index_col=0)
#     file_table = file.to_string()
#     return render_template('cafes.html', datatable=file_table)
#
#
# @app.route('/add')
# def add_page():
#     return render_template('add.html')
#
#
# if __name__ == "__main__":
#     app.run(debug="on")
