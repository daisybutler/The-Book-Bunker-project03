import os
from flask import (
        Flask, flash, render_template, redirect,
        request, session, url_for)

from flask_pymongo import PyMongo

from bson.objectid import ObjectId

# Security features from Werkzeug library
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/all-books")
def all_books():
    all_books = list(mongo.db.books.find())
    return render_template("all-books.html", all_books=all_books)


@app.route("/all-books/<book_url>")
def show_book(book_url):
    selected_book = {}
    books = mongo.db.books.find()
    for book in books:
        if book["book_url"] == book_url:
            selected_book = book
        return "<h2>" + selected_book["title"] + "</h2>"


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))

        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email")
        }
        mongo.db.users.insert_one(signup)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("dashboard", username=session["user"]))

    return render_template("signup.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    return render_template("logout.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


