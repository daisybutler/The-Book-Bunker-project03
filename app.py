import os
from flask import (
        Flask, flash, render_template, redirect,
        request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index.html")
def homepage():
    return render_template("index.html")


@app.route("/all-books.html")
def all_books():
    all_books = list(mongo.db.books.find())
    return render_template("all-books.html", all_books=all_books)


@app.route("/dashboard")
def dashboard():
    return render_template("/dashboard.html")


@app.route("/contact")
def contact():
    return render_template("/contact.html")


@app.route("/signup")
def signup():
    return render_template("/signup.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    return render_template("/logout.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


