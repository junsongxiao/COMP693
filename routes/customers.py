
from flask import render_template, request, redirect, url_for, flash
from app import app
from controller.customer_controllers import CustomerController
from controller.auth_controller import AuthController
from controller.user_controllers import UserController
from routes.session_utils import is_logged_in, is_admin, is_agent
from mysql.connector.errors import IntegrityError


@app.route('/customers')
def customers():
    all_customers = CustomerController.get_all_customers()
    return render_template('customers/customers.html', customers=all_customers)


@app.route('/edit_customer/<int:customer_id>', methods=['GET', 'POST'])
def edit_customer(customer_id):
    if not is_logged_in():
        return redirect(url_for('login'))
    if not is_admin():
        return redirect(url_for('dashboard'))
    
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
    if not is_logged_in():
        return redirect(url_for('login'))
    elif not (is_admin() or is_agent()):
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        # Extract form data
        username=request.form.get('username')
        password=request.form.get('password')
        confirm_password=request.form.get('confirm_password')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        wechat = request.form.get('wechat')
        preferences = request.form.get('preferences')
        notes = request.form.get('notes')
     
        # Validate password confirmation
        if password != confirm_password:
            flash("Passwords do not match.")
            return redirect(url_for('add_customer'))
        try:
            
            user_id=UserController.add_user(username,password,"Customer")
           
            user=CustomerController.create_customer(user_id, first_name, last_name, email, phone, wechat, preferences, notes)
                
            if user_id and user:
                flash("Customer added and credentials created successfully.")
                
                return redirect(url_for("customers"))
            else:
                flash("Failed to create customer details.")
        except IntegrityError as e:
            flash("Username already taken. Please choose a different username.")


    return render_template('customers/add_customer.html')

