from flask import render_template, redirect, url_for, session, flash
from app import app
from controller.auth_controller import AuthController
from controller.user_controllers import UserController
from model.users import Users
from routes.session_utils import is_logged_in, auth_handler


@app.route("/dashboard")
def dashboard():
    
    # allowed_roles = ["Admin", "Agent", "Customer","Guest"]
    # if not auth_handler(allowed_roles):

    #     print("Not logged in")
    #     return redirect(url_for("login"))
    if not is_logged_in():
        return redirect(url_for("login"))
    
    user_id = session.get("UserID")
    user_type=session.get('Type')
    
    print(user_id,user_type)
    if user_type=='Admin':
        user_details = UserController.get_admin_profile(user_id)
    elif user_type=='Agent':
        user_details = UserController.get_agent_profile(user_id)
    elif user_type=='Customer':
        user_details = UserController.get_customer_profile(user_id)
    else:
        return redirect(url_for('login'))
    
    if not user_details:
        flash("User details not found.")
        
        return redirect(url_for("login"))
    
    # name = f"{user_details.get('FirstName', '')} {user_details.get('LastName', '')}".strip()
    # role = user_details.get("Type", "Unknown")
    # return render_template("dashboard.html", name=name, role=role)

    return render_template('dashboard.html', user=user_details,user_type=user_type)
