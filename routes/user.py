from flask import Blueprint, render_template, request, redirect, url_for, session,flash
from controller.user_controllers import UserController
from routes.session_utils import is_logged_in, is_admin
from app import app
import bcrypt

# @app.route('/profile')
# def profile():
#     print("profile route")
#     if not is_logged_in():
#         return redirect(url_for('login'))

#     user_id = session.get('UserID')
#     user_type=session.get('Type')
#     print(user_id,user_type)

#     user = UserController.get_profile_details(user_id, user_type)
#     print(user)
#     return render_template('profile/profile.html', user=user)
#     # return render_template('profile/profile.html')

@app.route('/profile')
def profile():
    if not is_logged_in():
        return redirect(url_for('login'))

    user_id = session.get('UserID')
    user_type = session.get('Type')
    print(user_id,user_type )
    if user_type=='Admin':
        user=UserController.get_admin_profile(user_id)
    elif user_type=='Agent':
        user=UserController.get_agent_profile(user_id)
    elif user_type=='Customer':
        user=UserController.get_customer_profile(user_id)
    else:
        return redirect(url_for('login'))

    
    return render_template('profile/profile.html', user=user,user_type=user_type)

@app.route('/users')
def users():
    if not is_logged_in():
        return redirect(url_for('login'))
    elif not is_admin():
        return redirect(url_for('dashboard'))
    users = UserController.get_all_users()
    return render_template('users/users.html', users=users)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    user_id = session.get('UserID')
    user_type = session.get('Type')
  
    if not is_logged_in:
        return redirect(url_for('login'))

    if request.method == 'POST':
       
        # Common fields
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        wechat = request.form.get('wechat')
        
        # Update profile based on user type
        if user_type == 'Customer':
            UserController.update_customer_profile(user_id, first_name, last_name, email, phone, wechat)
        elif user_type == 'Agent':
            UserController.update_agent_profile(user_id, first_name, last_name, email, phone, wechat)
        elif user_type == 'Admin':
            UserController.update_admin_profile(user_id, first_name, last_name, email, phone, wechat)
    
    if user_type == 'Customer':
        profile= UserController.get_customer_profile(user_id)
    elif user_type == 'Agent':
        profile=UserController.get_agent_profile(user_id)
    elif user_type == 'Admin':
        profile=UserController.get_admin_profile(user_id)
    
   
    return render_template('profile/edit_profile.html', profile=profile, user_type=user_type)

@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):

    if not is_logged_in():
        flash('You must be logged in as an admin to access this page.')
        return redirect(url_for('login'))
    
    if not is_admin():
        flash('You do not have permission to access this page.')
        return redirect(url_for('dashboard'))
    
    # if request.method == 'POST':
    #     # user_id= request.form.get('UserID')
    #     username = request.form.get('user_name')
    #     password = request.form.get('password')
    #     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")
    #     user_type = request.form.get('new_type')
    #     return UserController.update_user(user_id, username,hashed_password, user_type)
    if request.method == 'POST':
        username = request.form.get('user_name')  # Corrected field name
        password = request.form.get('password')  # Kept as is, consider conditional hashing
        user_type = request.form.get('new_type')  # Corrected field name

        hashed_password = None
        if password:  # Only hash if a new password is provided
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")

        # return UserController.update_user(user_id, username, hashed_password, user_type)
        result = UserController.update_user(user_id, username, hashed_password, user_type)
        if result:
            flash('User updated successfully.')
            return redirect(url_for('users'))
        else:
            flash('Failed to update user.')
            return redirect(url_for('users'))

    
    user = UserController.get_user_by_id(user_id)
    return render_template('users/edit_user.html', user=user)
        
    
