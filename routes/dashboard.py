from flask import render_template, redirect, url_for, session, flash
from app import app
from controller.auth_controller import AuthController
from controller.user_controllers import UserController
from model.users import Users
from routes.session_utils import is_logged_in, auth_handler


@app.route("/dashboard")
def dashboard():
    # Check if user is logged in

    print(session)
    allowed_roles = ["Admin", "Agent", "Customer","Guest"]
    auth_handler(allowed_roles)
    print(auth_handler(allowed_roles))
    print(session)
    user_id = session.get("UserID")
    print(user_id)
    if not user_id:
        flash("User not found. Please log in.")
        print("User not found. Please log in.")
        return redirect(url_for("login"))

    user_details = UserController.get_user_role_details(user_id)
    print(user_details)
    if not user_details:
        flash("User details not found.")
        print("User details not found.")
        return redirect(url_for("login"))
    
    name = f"{user_details.get('FirstName', '')} {user_details.get('LastName', '')}".strip()
    role = user_details.get("Type", "Unknown")

    print(name)
    print(role)
    
    return render_template("dashboard.html", name=name, role=role)
