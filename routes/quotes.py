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

    return render_template('my_bookings.html', bookings=bookings, user_role=user_role)

@app.route('/quote_inquiry/<int:booking_id>', methods=['GET', 'POST'])
def quote_inquiry(booking_id):
    
    if not (is_agent() or is_admin()):
        
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Extract form data
        quoted_adult_price = request.form.get('quoted_adult_price')
        quoted_child_price = request.form.get('quoted_child_price')
        quoted_infant_price = request.form.get('quoted_infant_price')
        quoted_family_price = request.form.get('quoted_family_price')
        notes = request.form.get('notes')

        # Update quoted prices and notes
        success = BookingController.process_quote(
            booking_id, quoted_adult_price, quoted_child_price, 
            quoted_infant_price, quoted_family_price, notes
        )
       

        if success:
            BookingController.update_status(booking_id, 'Quote')
            flash('Quote successfully submitted. Booking ID: ' + str(booking_id) + '. You can check the quotation from All quotes.')
        else:
            flash('Failed to submit quote.')

        return redirect(url_for('inquiries'))

    inquiry = BookingController.get_inquiry_details(booking_id)
    if inquiry:
        return render_template('quotes/quote_inquiry.html', inquiry=inquiry)
    else:
        flash('Inquiry not found.')
        return redirect(url_for('inquiries'))



# @app.route('/update_inquiry_status/<int:booking_id>', methods=['POST'])
# def update_inquiry_status(booking_id):
#     if not is_agent():
#         flash("Unauthorized access.", "error")
#         return redirect(url_for('login'))

#     new_status = request.form.get('new_status')
#     quoted_prices = {
#         'quoted_adult_price': request.form.get('quoted_adult_price'),
#         'quoted_child_price': request.form.get('quoted_child_price'),
#         'quoted_infant_price': request.form.get('quoted_infant_price'),
#         'quoted_family_price': request.form.get('quoted_family_price')
#     }

#     # Check for missing status update
#     if not new_status:
#         flash("Status update failed. Invalid status provided.", "error")
#         return redirect(url_for('agent_inquiries'))

#     # Update quoted prices and status
#     prices_updated = BookingController.update_quoted_prices(booking_id, quoted_prices)
#     status_updated = BookingController.update_inquiry_status(booking_id, new_status)

#     if prices_updated and status_updated:
#         flash("Inquiry status and prices updated successfully.", "success")
#     else:
#         flash("Failed to update inquiry status and/or prices.", "error")

#     return redirect(url_for('agent_inquiries'))

@app.route('/quotes')
def quotes():
    if not (is_agent() or is_admin()):
        return redirect(url_for('login'))

    all_quotes = BookingController.get_all_quotes()
    return render_template('bookings/quotes.html', quotes=all_quotes)




@app.route('/send_quote_email/<int:booking_id>')
def send_quote_email(booking_id):
    # Retrieve the quote details
    print("rendering template for sending email")
    quote = BookingController.get_quote_details(booking_id)
    print(quote)
   

    if quote:
        print("sending email")
        # Prepare email content
        subject = "Your Quote Details"
        recipient = [quote['CustomerEmail']]  # Assuming you have customer email in the quote details
        body = f"""
        Dear {quote['FirstName']} {quote['LastName']},

        Here are your quote details for the {quote['TourName']}:
        
        
        - Adults: {quote['AdultNum']} x {quote['AdultQuote']} = {quote['AdultNum'] * quote['AdultQuote']}
        - Children: {quote['ChildNum']} x {quote['ChildQuote']} = {quote['ChildNum'] * quote['ChildQuote']}
        - Infants: {quote['InfantNum']} x {quote['InfantQuote']} = {quote['InfantNum'] * quote['InfantQuote']}
        - Families: {quote['FamilyNum']} x {quote['FamilyQuote']} = {quote['FamilyNum'] * quote['FamilyQuote']}
        - Total Quote: {quote['AdultNum'] * quote['AdultQuote'] + quote['ChildNum'] * quote['ChildQuote'] + quote['InfantNum'] * quote['InfantQuote'] + quote['FamilyNum'] * quote['FamilyQuote']}
        - Tour Date: {quote['TourDate']}
        - Notes: {quote['Note']}

        Please feel free to contact us for any further information or clarification.

        Best Regards,
        NZ EASYTOUR Team
        """
        


        # Sending email
        try:
            print("sending email")
            msg = Message(subject, sender=app.config['MAIL_DEFAULT_SENDER'], recipients=recipient)
            msg.body = body
            mail.send(msg)
            flash('Email sent successfully to customer.')
        except Exception as e:
            flash(f'Failed to send email: {str(e)}')

        return redirect(url_for('quotes'))
    else:
        flash('Quote not found.')
        return redirect(url_for('quotes'))


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


@app.route('/agent_quotes')
def agent_quotes():
    if not is_agent():
        return redirect(url_for('login'))

    agent_id = session.get('UserID')
    quotes = BookingController.get_agent_quotes(agent_id)
    return render_template('bookings/agent_quotes.html', quotes=quotes)

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


@app.route('/add_quote', methods=['GET', 'POST'])
def add_quote():
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

        

        if BookingController.add_booking(customer_id, tour_id,agent_id,confirmation_num, booking_account_name,booking_names,tour_date, adult_num, child_num, infant_num, family_num, adult_quote,child_quote,infant_quote,family_quote,pickup_location, note,'Quote'):
            flash('Quote added successfully')
            return redirect(url_for('quotes'))
        else:
            flash('Failed to add booking')

    customers = CustomerController.get_all_customers()
    tours = TourController.get_all_tours()
    agents = AgentController.get_all_agents()
    return render_template('bookings/add_quote.html', customers=customers, tours=tours, agents=agents, user_type=user_type)












