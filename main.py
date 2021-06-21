from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(200), nullable=False, unique=True)
    author = db.Column(db.VARCHAR(200), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


@app.route('/')
def home():
    book_data = db.session.query(Book).all()
    length = len(book_data)
    return render_template("index.html", databook=book_data, leng=length)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book = Book(title=request.form["title"],
                    author=request.form["author"],
                    rating=request.form["rating"])
        db.session.add(book)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html")


@app.route("/edit", methods=["POST", "GET"])
def edit():
    id_book = request.args.get("id_book")
    book = Book.query.get(id_book)

    if request.method == "POST":
        rating_after = request.form["rating_after"]
        book.rating = float(rating_after)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", thisbook=book)


@app.route("/delete")
def delete():
    id_book = request.args.get("id_delete")
    book = Book.query.get(int(id_book))
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

