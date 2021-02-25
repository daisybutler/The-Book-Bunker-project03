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


# DISPLAY HOME -------------------------------------
@app.route("/")
def home():
    # Passes in username to display session user when applicable
    return render_template("index.html")


# DISPLAY ALL BOOKS -------------------------------------
@app.route("/all-books")
def all_books():
    all_books = list(mongo.db.books.find())
    return render_template("all-books.html", all_books=all_books)


# DISPLAY INDIVIDUAL BOOKS -------------------------------------
@app.route("/display-book/<book_id>")
def display_book(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    selected_book = {"title": book["title"],
                     "author": book["author"], "category": book["category"],
                     "year": book["year"], "image_url": book["image_url"],
                     "description": book["description"]}
    return render_template("display-book.html", selected_book=selected_book)


# DISPLAY USER DASHBOARD -------------------------------------
@app.route("/dashboard/<username>", methods=['GET', 'POST'])
def dashboard(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("dashboard.html", username=username)


# DISPLAY CONTACT -------------------------------------
@app.route("/contact")
def contact():
    return render_template("contact.html")


# SEARCH ALL BOOKS -------------------------------------
@app.route("/search-categories", methods=["GET", "POST"])
def search_categories():
    search = request.form.get('search')
    all_books = list(mongo.db.books.find({"$text": {"$search": search}}))
    return render_template("all-books.html", all_books=all_books)


# SIGNUP -------------------------------------
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


# LOGIN -------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Checks if there is a matching username in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "dashboard", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# LOGOUT -------------------------------------
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
