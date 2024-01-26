from flask import request, redirect, url_for, flash, session, render_template
from app import app
from controller.booking_controllers import BookingController
from routes.session_utils import is_logged_in, auth_handler, is_agent

@app.route('/inquire', methods=['POST'])
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

@app.route('/my_bookings')
def my_bookings():
    if not is_logged_in():
        return redirect(url_for('login'))

    user_id = session.get('UserID')
    bookings = BookingController.get_bookings_by_user(user_id)
    return render_template('my_bookings.html', bookings=bookings)

@app.route('/agent/inquiries')
def agent_inquiries():
    if not is_agent():
        return redirect(url_for('login'))

    agent_id = session.get('AgentID')
    inquiries =BookingController.get_agent_inquiries(agent_id)
    return render_template('agent_inquiries.html', inquiries=inquiries)

@app.route('/quote_inquiry/<int:booking_id>', methods=['GET', 'POST'])
def quote_inquiry(booking_id):
    if not is_agent():
        return redirect(url_for('login'))

    if request.method == 'POST':
        quoted_adult_price = request.form.get('quoted_adult_price')
        quoted_child_price = request.form.get('quoted_child_price')
        quoted_infant_price = request.form.get('quoted_infant_price')
        quoted_family_price = request.form.get('quoted_family_price')
        notes = request.form.get('notes')

        # Assuming a method to update quoted prices and notes exists in the BookingController
        success = BookingController.update_quoted_prices_and_notes(
            booking_id, quoted_adult_price, quoted_child_price, 
            quoted_infant_price, quoted_family_price, notes
        )

        if success:
            BookingController.update_booking_status(booking_id, 'Quote')
            flash('Quote successfully submitted.')
        else:
            flash('Failed to submit quote.')

        return redirect(url_for('agent_inquiries'))

    # Assuming a method to get inquiry details exists in the BookingController
    inquiry = BookingController.get_inquiry_details(booking_id)
    if inquiry:
        return render_template('quote_inquiry.html', inquiry=inquiry)
    else:
        flash('Inquiry not found.')
        return redirect(url_for('agent_inquiries'))



@app.route('/update_inquiry_status/<int:booking_id>', methods=['POST'])
def update_inquiry_status(booking_id):
    if not is_agent():
        flash("Unauthorized access.", "error")
        return redirect(url_for('login'))

    new_status = request.form.get('new_status')
    quoted_prices = {
        'quoted_adult_price': request.form.get('quoted_adult_price'),
        'quoted_child_price': request.form.get('quoted_child_price'),
        'quoted_infant_price': request.form.get('quoted_infant_price'),
        'quoted_family_price': request.form.get('quoted_family_price')
    }

    # Check for missing status update
    if not new_status:
        flash("Status update failed. Invalid status provided.", "error")
        return redirect(url_for('agent_inquiries'))

    # Update quoted prices and status
    prices_updated = BookingController.update_quoted_prices(booking_id, quoted_prices)
    status_updated = BookingController.update_inquiry_status(booking_id, new_status)

    if prices_updated and status_updated:
        flash("Inquiry status and prices updated successfully.", "success")
    else:
        flash("Failed to update inquiry status and/or prices.", "error")

    return redirect(url_for('agent_inquiries'))

@app.route('/agent_quotes')
def agent_quotes():
    if not is_agent():
        return redirect(url_for('login'))

    agent_id = session.get('UserID')
    quotes = BookingController.get_agent_quotes(agent_id)
    return render_template('agent_quotes.html', quotes=quotes)





