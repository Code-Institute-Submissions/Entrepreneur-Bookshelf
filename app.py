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
                flash("Welcome, {}".format(request.form.get("username")))
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
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Let's remove the reader from the session cookies
    flash("You have logged out! 👋🏼")
    session.pop("reader")
    return redirect(url_for("login"))


@app.route("/add_book")
def add_book():
    return render_template("add_book.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(
        os.environ.get("PORT")), debug=True)
