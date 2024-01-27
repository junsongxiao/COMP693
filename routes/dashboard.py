from flask import render_template, redirect, url_for, session
from routes.session_utils import auth_handler, is_logged_in
from app import app
from model.users import Users

@app.route("/dashboard")
def dashboard():
    # Check if user is logged in
    auth_handler(["Admin","Agent", "Customer","Guest"])  # List of allowed roles
    role, user = Users.get_user_role_details(session["user_id"])
    
    name = f"{user['title']} {user['first_name']} {user['last_name']}".strip()
    
    return render_template("dashboard.html", name=name, role=role)


