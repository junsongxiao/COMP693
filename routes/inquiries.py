from flask import request, redirect, url_for, flash, session, render_template
from app import app, mail
from controller.booking_controllers import BookingController
from controller.customer_controllers import CustomerController
from controller.tour_controllers import TourController
from controller.agent_controllers import AgentController
from routes.session_utils import is_logged_in, auth_handler, is_agent, is_admin
from flask_mail import Message, Mail


@app.route('/inquire', methods=['GET','POST'])
def inquire():
    if not is_logged_in():
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
    print("rendering inquiries")
   
    # Check if the user is either an agent or an admin
    if not (is_agent() or is_admin()):
        return redirect(url_for('login'))
    
    
    print("rendering inquiries location 2")
    all_inquiries = BookingController.get_all_inquiries()
    print(all_inquiries)
    return render_template('bookings/inquiries.html', inquiries=all_inquiries)
