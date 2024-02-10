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
            preferences = request.form.get('preferences')
            notes = request.form.get('notes')
            success=UserController.update_customer_profile(user_id, first_name, last_name, email, phone, wechat,preferences,notes)
            if success:
                flash('Profile updated successfully.')
            else:
                flash('Failed to update profile.')
                return redirect(url_for('edit_profile'))
            
        elif user_type == 'Agent':
            agency_name = request.form.get('agency_name')
            success=UserController.update_agent_profile(user_id, first_name, last_name, email, phone, wechat,agency_name)
            if success:
                flash('Profile updated successfully.')
            else:
                flash('Failed to update profile.')
                return redirect(url_for('edit_profile'))
        elif user_type == 'Admin':
            success=UserController.update_admin_profile(user_id, first_name, last_name, email, phone, wechat)
            if success:
                flash('Profile updated successfully.')
            else:
                flash('Failed to update profile.')
                return redirect(url_for('edit_profile'))
    
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
    elif not is_admin():
        flash('You do not have permission to access this page.')
        return redirect(url_for('dashboard'))
    elif request.method == 'POST':
         
        password = request.form.get('password')  
        confirm_password = request.form.get('confirm_password')

        # Validate password confirmation
        if password != confirm_password:
            flash("Passwords do not match.")
            return redirect(url_for('users'))
               

     
        if password:  # If password is provided, update password
            

            # return UserController.update_user(user_id, username, hashed_password, user_type)
            result = UserController.update_password(user_id, password)
            if result:
                flash('User password updated successfully.')
                return redirect(url_for('users'))
            else:
                flash('Failed to update password.')
                return redirect(url_for('users'))
        # elif user_type:
        #     result = UserController.update_type(user_id, user_type)
        #     if result:
        #         flash('User type updated successfully.')
        #         return redirect(url_for('users'))
        #     else:
        #         flash('Failed to update user type.')
        #         return redirect(url_for('users'))
       
        else:
            flash('No changes made.')
        

        
        user = UserController.get_user_by_id(user_id)
        return render_template('users/edit_user.html', user=user)
    else:
        user = UserController.get_user_by_id(user_id)
        return render_template('users/edit_user.html', user=user)

        
    
