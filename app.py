# Base of this code was inspired by CI To-Do list Mini-Project (https://github.com/Code-Institute-Solutions/TaskManagerAuth).
# Code base was modified and adapted to meet the project's need.

import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_books")
def get_books():
    books = list(mongo.db.books.find())
    return render_template("books.html", books=books)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books = list(mongo.db.books.find({"$text": {"$search": query}}))
    return render_template("books.html", books=books)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Let's check if the username already exists in the database
        existing_reader = mongo.db.readers.find_one(
            {"username": request.form.get("username").lower()})

        if existing_reader:
            flash("🤦🏼‍♂️ This reader's username already exists. Please, try again.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.readers.insert_one(register)

        # Let's put the new user into their 'session' cookie
        session["reader"] = request.form.get("username").lower()
        flash("🎉 Successful Registration!")
        return redirect(url_for("profile", username=session["reader"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Let's check if the username exists in the database
        existing_reader = mongo.db.readers.find_one(
            {"username": request.form.get("username").lower()})

        if existing_reader:
            # Let's make sure the hashed password matches the user input
            if check_password_hash(existing_reader["password"],
                                   request.form.get("password")):
                session["reader"] = request.form.get("username").lower()
                flash("Welcome, {} 😃".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["reader"]))

            else:
                # Let's let them know something is not right
                flash("🤔 Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Let's let them know something is not right
            flash("🤔 Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Let's grab the session user's username from the database
    username = mongo.db.readers.find_one(
        {"username": session["reader"]})["username"]

    if session["reader"]:
        books = list(mongo.db.books.find())
        return render_template("profile.html", username=username, books=books)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Let's remove the reader from the session cookies
    flash("You have logged out! 👋🏼")
    session.pop("reader")
    return redirect(url_for("login"))


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        is_priority = "on" if request.form.get("is_priority") else "off"
        book = {
            "category_name": request.form.get("category_name"),
            "book_title": request.form.get("book_title"),
            "book_author": request.form.get("book_author"),
            "is_priority": is_priority,
            "read_by_date": request.form.get("read_by_date"),
            "added_by": session["reader"]
        }
        mongo.db.books.insert_one(book)
        flash("📚 Book Successfully Added")
        return redirect(url_for("get_books"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_book.html", categories=categories)


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        is_priority = "on" if request.form.get("is_priority") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "book_title": request.form.get("book_title"),
            "book_author": request.form.get("book_author"),
            "is_priority": is_priority,
            "read_by_date": request.form.get("read_by_date"),
            "added_by": session["reader"]
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, submit)
        flash("📚 Book Successfully Updated")
        return redirect(url_for("get_books"))

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_book.html", book=book, categories=categories)


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Book Successfully Removed 👀")
    return redirect(url_for("get_books"))


@app.route("/get_categories")
def get_categories():
    username = mongo.db.readers.find_one(
        {"username": session["reader"]})["username"]
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories, username=username)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("🔖 New Category Added")
        return redirect(url_for("get_categories"))

    username = mongo.db.readers.find_one(
        {"username": session["reader"]})["username"]
    return render_template("add_category.html", username=username)


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("🔖 Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    username = mongo.db.readers.find_one(
        {"username": session["reader"]})["username"]
    return render_template("edit_category.html", category=category, username=username)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Removed 👀")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(
        os.environ.get("PORT")), debug=False)
