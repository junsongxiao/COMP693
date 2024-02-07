from flask import request, redirect, url_for, flash, session, render_template
from app import app, mail
from controller.booking_controllers import BookingController
from controller.customer_controllers import CustomerController
from controller.tour_controllers import TourController
from controller.agent_controllers import AgentController
from routes.session_utils import is_logged_in, auth_handler, is_agent, is_admin
from flask_mail import Message, Mail



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



@app.route('/quotes')
def quotes():
    if not (is_agent() or is_admin()):
        return redirect(url_for('login'))

    all_quotes = BookingController.get_all_quotes()
    return render_template('quotes/quotes.html', quotes=all_quotes)




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



@app.route('/agent_quotes')
def agent_quotes():
    if not is_agent():
        return redirect(url_for('login'))

    agent_id = session.get('UserID')
    quotes = BookingController.get_agent_quotes(agent_id)
    return render_template('quotes/agent_quotes.html', quotes=quotes)


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
            flash('Failed to add quote')

    customers = CustomerController.get_all_customers()
    tours = TourController.get_all_tours()
    agents = AgentController.get_all_agents()
    return render_template('quotes/add_quote.html', customers=customers, tours=tours, agents=agents, user_type=user_type)












