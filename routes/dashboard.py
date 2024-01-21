from flask import render_template, redirect, url_for, session
from routes.session_utils import auth_handler, is_logged_in
from app import app
import model.user

@app.route("/dashboard")
def dashboard():
    # Check if user is logged in
    auth_handler(["doctor", "nurse", "patient", "receptionist", "admin"])  # List of allowed roles
    role, user = model.user.get_user_role_details(session["user_id"])
    
    name = f"{user['title']} {user['first_name']} {user['last_name']}".strip()
    
    return render_template("dashboard.html", name=name, role=role)


