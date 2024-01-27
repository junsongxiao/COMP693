# routes/auth.py

from flask import render_template, request, redirect, url_for, session, flash
from app import app
from controller.auth_controller import AuthController

@app.route("/login", methods=["GET", "POST"])
def login():
    if AuthController.is_logged_in():
        print("already logged in")
        return redirect(url_for("dashboard"))  # Redirect to dashboard if already logged in

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if AuthController.log_in(username, password):
            flash("Login successfully!")
            print("Login successfully!")
            return redirect(url_for("dashboard"))  # Redirect to dashboard after successful login
        else:
            print("invlaid username or password")
            flash("Invalid username or password.")

    print("login failed")
    return render_template("auth/login.html")  # Show login page for GET request or failed login


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user_type = request.form.get("type")  # Or however you determine user type
        if AuthController.register_user(username, password, user_type):
            flash("Registration successful.")
            return redirect(url_for("login"))
        else:
            flash("Registration failed.")
    return render_template("auth/register.html")

@app.route("/logout")
def logout():
    AuthController.log_out()
    flash("You have been logged out.")
    return redirect(url_for("login"))
