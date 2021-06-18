from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message="You must be at least 4 characters long"),
                                             Length(min=4)])
    password = PasswordField('Password', validators=[DataRequired(message="You must be at least 8 characters long"), Length(min=3)])
    submit = SubmitField(label="Submit")


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "123"


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@gmail.com" and login_form.password.data == "123":
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=login_form)



if __name__ == '__main__':
    app.run(debug="on")

