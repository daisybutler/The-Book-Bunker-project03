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
                     "description": book["description"],
                     "purchase_link": book["purchase_link"],
                     "added_by": book["added_by"]
                     }
    return render_template("display-book.html", selected_book=selected_book)


# ADD BOOK -------------------------------------
@app.route("/add-book", methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = {
            "title": request.form.get("title").title(),
            "author": request.form.get("author").title(),
            "category": request.form.get("category_name"),
            "year": request.form.get("year"),
            "image_url": request.form.get("image_url"),
            "description": request.form.get("description"),
            "purchase_link": request.form.get("purchase_link"),
            "added_by": session["user"]
        }
        mongo.db.books.insert_one(new_book)
        flash("Book added")
        return redirect(url_for('all_books'))

    categories = mongo.db.categories.find().sort('category_name', 1)
    return render_template("add-book.html", categories=categories)


# DISPLAY USER DASHBOARD -------------------------------------
@app.route("/dashboard/<username>", methods=['GET', 'POST'])
def dashboard(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    recommended_books = mongo.db.books.find({"added_by": session['user']})

    """all_books = mongo.db.books.find()
    user_saved = mongo.db.users.find_one('saved_books')
    saved_books_dict = {}

    for val in user_saved.values():
        for item in val:
            for book in all_books:
                if book["_id"] == item:
                    saved_books_dict[val] = book"""

    return render_template("dashboard.html", username=username,
                           recommended_books=recommended_books)


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
