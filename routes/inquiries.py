from flask import request, redirect, url_for, flash, session, render_template
from app import app, mail
from controller.booking_controllers import BookingController
from controller.customer_controllers import CustomerController
from controller.tour_controllers import TourController
from controller.agent_controllers import AgentController
from routes.session_utils import is_logged_in, auth_handler, is_agent, is_admin, is_customer
from flask_mail import Message, Mail


@app.route('/inquire', methods=['GET','POST'])
def inquire():
    if not is_logged_in():
        flash('Please log in to make an inquiry.')
        return redirect(url_for('login'))

    inquiry_details = {
        'tour_id': request.form.get('tour_id'),
        'selected_date': request.form.get('selected_date'),
        'adult_num': request.form.get('adult_num'),
        'child_num': request.form.get('child_num'),
        'infant_num': request.form.get('infant_num'),
        'family_num': request.form.get('family_num'),
        'pickup_location': request.form.get('pickup_location'),
        'note': request.form.get('note'),
        'booking_account_name': request.form.get('booking_account_name'),
        'booking_names': request.form.get('booking_names'),
        'user_id': session.get('UserID')
    }

    # Check if the essential details are present
    if not inquiry_details['tour_id'] or not inquiry_details['selected_date']:
        flash('Invalid tour or date selected.')
        return redirect(url_for('tours'))

    booking_id = BookingController.add_inquiry(**inquiry_details)

    if booking_id:
        flash('Inquiry submitted successfully. Booking ID: ' + str(booking_id))
    else:
        flash('Failed to submit inquiry.')
    return redirect(url_for('tours'))


@app.route('/inquiries')
def inquiries():
    
   
    # Check if the user is either an agent or an admin
    if not (is_agent() or is_admin()):
        return redirect(url_for('login'))
    
    
   
    all_inquiries = BookingController.get_all_inquiries()
    
    return render_template('inquiries/inquiries.html', inquiries=all_inquiries)


# @app.route('/my_inquiries')
# def my_inquiries():
#     if not is_logged_in():
#         return redirect(url_for('login'))
#     elif not is_customer():
#         return redirect(url_for('dashboard'))
    
#     user_id = session['UserID']
#     customer_result = CustomerController.get_customer_id_by_user_id(user_id)
    
#     # Check if customer_result is not None and has 'CustomerID' key
#     if customer_result and 'CustomerID' in customer_result:
#         customer_id = customer_result['CustomerID']
#     else:
#         flash('Customer ID not found.')
#         return redirect(url_for('dashboard'))  # Or some other appropriate action

#     inquiries = BookingController.get_customer_inquiries(customer_id)
#     for inquiry in inquiries:
#         print(inquiry['TourName'], inquiry['OperatorName'])


#     if not inquiries:
#         flash('You have no inquiries.')
#     return render_template('inquiries/my_inquiries.html', inquiries=inquiries)
@app.route('/my_inquiries')
def my_inquiries():
    if not is_logged_in():
        return redirect(url_for('login'))
    elif not is_customer():
        return redirect(url_for('dashboard'))
    
    user_id = session['UserID']
    customer_id = CustomerController.get_customer_id_by_user_id(user_id)
    if customer_id:
        customer_id = customer_id['CustomerID']  # Assuming this returns a dict with CustomerID
        inquiries = BookingController.get_customer_inquiries(customer_id)
        
        for inquiry in inquiries:
            if 'TourName' in inquiry :
                print(inquiry['TourName'])
            else:
                print("Keys not found in inquiry:", inquiry)


        if not inquiries:
            flash('You have no inquiries.')
        return render_template('inquiries/my_inquiries.html', inquiries=inquiries)
    else:
        flash('Customer ID not found.')
        return redirect(url_for('dashboard'))
