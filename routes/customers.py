from flask import render_template, request, redirect, url_for, flash
from app import app
from controller.customer_controllers import CustomerController

@app.route('/customers')
def customers():
    all_customers = CustomerController.get_all_customers()
    return render_template('customers/customers.html', customers=all_customers)


@app.route('/edit_customer/<int:customer_id>', methods=['GET', 'POST'])
def edit_customer(customer_id):
    if request.method == 'POST':
        # Extract form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        wechat = request.form.get('wechat')
        preferences = request.form.get('preferences')
        notes = request.form.get('notes')

        # Update customer
        if CustomerController.update_customer(customer_id, first_name, last_name, email,phone, wechat, preferences, notes):
            flash('Customer updated successfully.')
            return redirect(url_for('customers'))  # Redirect to customer list or appropriate page
        else:
            flash('Failed to update customer.')
            return redirect(url_for('edit_customer', customer_id=customer_id))

    customer_details = CustomerController.get_customer_details(customer_id)
    if customer_details:
        return render_template('customers/edit_customer.html', customer=customer_details)
    else:
        flash('Customer not found.')
        return redirect(url_for('customers'))

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        # Extract form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        wechat = request.form.get('wechat')
        preferences = request.form.get('preferences')
        notes = request.form.get('notes')
        # Add other fields here

        # Call controller method to add customer
        if CustomerController.add_customer(first_name, last_name, email, phone, wechat, preferences, notes):
            flash('Customer added successfully.')
            return redirect(url_for('customers'))  
        else:
            flash('Failed to add customer.')

    return render_template('customers/add_customer.html')

