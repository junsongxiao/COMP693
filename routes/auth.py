from flask import render_template, request, redirect, url_for, session, flash
from app import app
from controller.auth_controller import AuthController

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if AuthController.log_in(username, password):
            return redirect(url_for("dashboard"))  # Replace with your dashboard route
        flash("Invalid username or password.")
    return render_template("auth/login.html")

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
    session.clear()  # Clear the user's session
    flash("You have been logged out.")
    return redirect(url_for("login"))  # Redirect to the login page

# from flask import render_template, request, redirect, url_for, session, flash
# from app import app
# import model.auth as auth

# from routes.session_utils import is_logged_in

# """
# This module contains the routes for the login, registration and logout pages.
# """

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     # Redirect to index if the user is already logged in
#     if is_logged_in():
#         return redirect(url_for("index"))

#     # If the request method is POST, attempt to log the user in
#     if request.method == "POST":
#         if auth.log_in(request.form.get("username"), request.form.get("password")):
            
#             return redirect(url_for("dashboard"))
#         else:
#             error_msg = "Invalid username or password. Please try again."
#             return render_template("auth/login.html", error_msg=error_msg)
#     # If the request method is GET, display the login form
#     else:
#         return render_template("auth/login.html")


# @app.route("/logout", methods=["GET", "POST"])
# def logout():
#     """Logs the user out"""
#     if is_logged_in():
#         session.clear()
#     return redirect(url_for("index"))
