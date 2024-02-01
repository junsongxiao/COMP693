from flask import request, redirect, url_for, flash, session, render_template
from app import app, mail
from controller.booking_controllers import BookingController
from controller.customer_controllers import CustomerController
from controller.tour_controllers import TourController
from controller.agent_controllers import AgentController
from routes.session_utils import is_logged_in, auth_handler, is_agent, is_admin
from flask_mail import Message, Mail


@app.route('/my_bookings')
def my_bookings():
    '''Display all bookings for the logged in user depending on their role'''
    if 'UserID' not in session:
        return redirect(url_for('login'))

    user_id = session['UserID']
    user_role = session['Type']  

    if user_role == 'Agent':
        bookings = BookingController.get_agent_bookings(user_id)
    elif user_role == 'Customer':
        bookings = BookingController.get_customer_bookings(user_id)
    else:
        
        flash('Unable to determine your role.')
        return redirect(url_for('dashboard'))

    return render_template('bookings/my_bookings.html', bookings=bookings, user_role=user_role)

@app.route('/update_booking_status/<int:booking_id>', methods=['POST'])
def update_booking_status(booking_id):
    new_status = request.form.get('new_status')

    if BookingController.update_status(booking_id, new_status):
        flash('Booking status updated successfully.')
    else:
        flash('Failed to update booking status.')

    referrer = request.referrer or url_for('dashboard')  # Fallback to a default route if referrer is None
    return redirect(referrer)

    # return redirect(url_for('quotes'))  # Redirect to the quotes page or relevant page


@app.route('/all_bookings')
def all_bookings():
    if not (is_agent() or is_admin()):
        return redirect(url_for('login'))

    all_bookings = BookingController.get_all_bookings_except_inquiry_quote()
    return render_template('bookings/bookings.html', bookings=all_bookings)

@app.route('/edit_booking/<int:booking_id>', methods=['GET', 'POST'])
def edit_booking(booking_id):
    if request.method == 'POST':
        # Group form data into a dictionary
        booking_data = {
            "booking_account_name": request.form.get('booking_account_name'),
            "booking_names": request.form.get('booking_names'),
            "confirmation_num": request.form.get('confirmation_num'),
            "adult_quote": request.form.get('adult_quote'),
            "child_quote": request.form.get('child_quote'),
            "infant_quote": request.form.get('infant_quote'),
            "family_quote": request.form.get('family_quote'),
            "tour_date": request.form.get('tour_date'),
            "adult_num": request.form.get('adult_num'),
            "child_num": request.form.get('child_num'),
            "infant_num": request.form.get('infant_num'),
            "family_num": request.form.get('family_num'),
            "pick_up_location": request.form.get('pick_up_location'),
            "note": request.form.get('note')
        }

        # Update booking with the collected data
        if BookingController.update_booking(booking_id, **booking_data):
            flash('Booking updated successfully.')
            return redirect(url_for('all_bookings'))  
        else:
            flash('Failed to update booking.')
            return redirect(url_for('edit_booking', booking_id=booking_id))

    booking_details = BookingController.get_booking_details(booking_id)
    if booking_details:
        return render_template('bookings/edit_booking.html', booking=booking_details)
    else:
        flash('Booking not found.')
        return redirect(url_for('dashboard'))
    
@app.route('/add_booking', methods=['GET', 'POST'])
def add_booking():
    if not (is_agent() or is_admin()):
        return redirect(url_for('login'))
    user_type = session.get('user_type') 

    if request.method == 'POST':
        customer_id = request.form['CustomerID']
        tour_id = request.form['TourID']
        agent_id= request.form['AgentID']
        confirmation_num = request.form['ConfirmationNum']
        booking_account_name = request.form['BookingAccountName']
        booking_names= request.form['BookingNames']
        booking_num= request.form['BookingNum']

        tour_date = request.form['TourDate']
        adult_num = request.form['AdultNum']
        child_num = request.form['ChildNum']
        infant_num = request.form['InfantNum']
        family_num = request.form['FamilyNum']

        adult_quote = request.form['AdultQuote']
        child_quote = request.form['ChildQuote']
        infant_quote = request.form['InfantQuotee']
        family_quote = request.form['FamilyQuote']

        pickup_location = request.form['PickupLocation']
        note = request.form['Note']

        booking_status=request.form['BookingStatus']

        if BookingController.add_booking(customer_id, tour_id,agent_id,confirmation_num, booking_account_name,booking_names,tour_date, adult_num, child_num, infant_num, family_num, adult_quote,child_quote,infant_quote,family_quote,pickup_location, note,booking_status):
            flash('Booking added successfully')
            return redirect(url_for('dashboard'))
        else:
            flash('Failed to add booking')

    customers = CustomerController.get_all_customers()
    tours = TourController.get_all_tours()
    agents = AgentController.get_all_agents()
    return render_template('bookings/add_booking.html', customers=customers, tours=tours, agents=agents,user_type=user_type)











