# routes/auth.py
from flask import render_template, request, redirect, url_for, session, flash
from routes.session_utils import auth_handler, is_logged_in, is_agent
from app import app
# from model.users import Users
from model.auth import Auth
from controller.user_controllers import UserController
from controller.auth_controller import AuthController
from mysql.connector.errors import IntegrityError


@app.route("/login", methods=["GET", "POST"])
def login():
    
    if is_logged_in():
        print("Already logged in")
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if AuthController.log_in(username, password):
            print("Login successful, redirecting to dashboard")
            return redirect(url_for("dashboard"))
        else:
            print("Invalid username or password")
            flash("Invalid username or password.")

    print("Rendering login form")
    return render_template("auth/login.html")

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    """Logs the user out"""
    if is_logged_in():
        session.clear()
        flash("You have been logged out.")
    return redirect(url_for("home"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Gather form data
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        phone = request.form.get("phone_number")
        wechat = request.form.get("wechat")

        # Validate password confirmation
        if password != confirm_password:
            flash("Passwords do not match.")
            return render_template("auth/register.html")

        try:
            # Create user and get user_id
            user_id = Auth.create_user(username, password)
            if user_id:
                # Create customer details
                if UserController.create_customer(user_id, first_name, last_name, email, phone, wechat):
                    flash("Registration successful.")
                    return redirect(url_for("login"))
                else:
                    flash("Failed to create customer details.")
        except IntegrityError as e:
            flash("Username already taken. Please choose a different username.")
        
    return render_template("auth/register.html")
