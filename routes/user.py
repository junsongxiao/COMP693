from flask import Blueprint, render_template, request, redirect, url_for, session,flash
from controller.user_controllers import UserController
from routes.session_utils import is_logged_in
from app import app

@app.route('/profile')
def profile():
    if not is_logged_in():
        return redirect(url_for('login'))

    user_id = session.get('UserID')
    user_profile = UserController.get_user_profile(user_id)
    return render_template('profile.html', user=user_profile)


# @app.route('/edit_profile', methods=['GET', 'POST'])
# def edit_profile():
#     if not is_logged_in():
#         return redirect(url_for('login'))

#     user_id = session.get('UserID')

#     if request.method == 'POST':
#         first_name = request.form.get('first_name')
#         last_name = request.form.get('last_name')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         wechat = request.form.get('wechat')
#         preferences = request.form.get('preferences')
#         notes = request.form.get('notes')

#         success = UserController.update_user_profile(user_id, first_name, last_name, email, phone, wechat, preferences, notes)

#         if success:
#             flash('Profile updated successfully.')
#             return redirect(url_for('profile'))
#         else:
#             flash('Failed to update profile.')

#     user_profile = UserController.get_user_profile(user_id)
#     return render_template('edit_profile.html', user=user_profile)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    user_id = session.get('UserID')
    user_type = session.get('Type')
    if not user_id:
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
        

    profile_details = UserController.get_profile_details(user_id, user_type)
    return render_template('profile/edit_profile.html', profile=profile_details, user_type=user_type)

