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
    return render_template("index.html")


# DISPLAY ALL BOOKS -------------------------------------
@app.route("/all-books")
def all_books():
    all_books = list(mongo.db.books.find())
    style = "display:none"
    return render_template("all-books.html", all_books=all_books, style=style)


# DISPLAY INDIVIDUAL BOOKS -------------------------------------
@app.route("/display-book/<book_id>")
def display_book(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    selected_book = {"_id": book["_id"], "title": book["title"],
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
        {"username": session["user"]})['username']

    # Books the session user has added to the site themselves
    recommended_books = mongo.db.books.find({"added_by": session['user']})

    # All the key, value pairs associated with the session user in db
    user = mongo.db.users.find_one({"username": session["user"]})

    # Fetches books from the db which have IDs matching
    # those listed in the user's 'bookmarked' key
    user_bookmarked = user['bookmarked']
    bookmarked_books = []
    for book_id in user_bookmarked:
        book = mongo.db.books.find({"_id": ObjectId(book_id)})

        # Unpacks the cursor object returned by the find() method
        for item in book:
            bookmarked_books.append(item)

    return render_template("dashboard.html", username=username,
                           recommended_books=recommended_books,
                           bookmarked_books=bookmarked_books)


# BOOKMARK BOOK -------------------------------------
@app.route("/bookmark/<book_id>")
def bookmark(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    saved_book = {"_id": book["_id"], "title": book["title"],
                  "author": book["author"],
                  "category": book["category"],
                  "year": book["year"],
                  "image_url": book["image_url"],
                  "description": book["description"],
                  "purchase_link": book["purchase_link"],
                  "added_by": book["added_by"]
                  }

    # Successfully appends the book id to the bookmarked field
    # (flashed on screen) but doesnt seem to post to db
    user = mongo.db.users.find_one({"username": session["user"]})
    user['bookmarked'].append(book_id)
    flash(user['bookmarked'])

    return render_template("display-book.html", selected_book=saved_book)


# EDIT BOOK -------------------------------------
@app.route('/edit-book<book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    if request.method == 'POST':
        edited_book = {
            "title": request.form.get("title").title(),
            "author": request.form.get("author").title(),
            "category": request.form.get("category_name"),
            "year": request.form.get("year"),
            "image_url": request.form.get("image_url"),
            "description": request.form.get("description"),
            "purchase_link": request.form.get("purchase_link"),
            "added_by": session["user"]
        }
        mongo.db.books.update({'_id': ObjectId(book_id)}, edited_book)
        flash("Book edited")
        return redirect(url_for('dashboard', username=session["user"]))

    book = mongo.db.books.find_one({'_id': ObjectId(book_id)})
    categories = mongo.db.categories.find().sort('category_name', 1)
    return render_template("edit-book.html", categories=categories, book=book)


# DELETE BOOK -------------------------------------
@app.route('/delete-book<book_id>', methods=['GET', 'POST'])
def delete_book(book_id):
    mongo.db.books.remove({'_id': ObjectId(book_id)})
    flash("Book deleted")
    return redirect(url_for('dashboard', username=session["user"]))


"""
# LIKE BOOK ----------------------------------------
@app.route('/like_book', methods=['POST', 'GET'])
def like_book(book_id):
    like_count = mongo.db.books.find_one(
        {'_id': ObjectId(book_id)})["like_count"]
    if request.method == 'POST':
        like_count += 1
    else:
        flash('Whoops, something when wrong.')
    return flash('Liked')
    """


# SEARCH ALL BOOKS -------------------------------------
@app.route("/search-categories", methods=["GET", "POST"])
def search_categories():
    
    # Gets the keyword inputted by user in the search bar
    search = request.form.get('search')

    # Finds any value in book collection which contains text matching input
    all_books = list(mongo.db.books.find({"$text": {"$search": search}}))

    # Changes display of Show All Books button from 'none' to 'inline'
    style = "display: inline"

    # Conditonal check for feedback to give the user after search request
    if len(all_books) == 0:

        # If no results match the search word, return string below
        user_message = "Sorry, we couldn't find any results for '" + search + "'."
    else:
        # If results match the search word, return strong below
        user_message = "Showing results for '" + search + "'."

    # Display All Books page but only with those matching user's search
    return render_template("all-books.html", all_books=all_books,
                           style=style, user_message=user_message)


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
    return render_template('logout.html')


@app.route("/confirm_logout")
def confirm_logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
