from flask import request, redirect, url_for, flash, session, render_template
from app import app, mail
from controller.operator_controllers import OperatorController
from routes.session_utils import is_logged_in, auth_handler, is_agent, is_admin

@app.route('/operators_list')
def operators_list():
    # Assuming the user needs to be an admin to access this page
    if not is_admin():
        return redirect(url_for('login'))

    operators = OperatorController.get_all_operators()
    return render_template('operators/operators.html', operators=operators)


@app.route('/edit_operator/<int:operator_id>', methods=['GET', 'POST'])
def edit_operator(operator_id):
    if not is_logged_in():
        flash('You must be logged in to access this page.')
        return redirect(url_for('login'))
    elif not is_admin():
        flash('You do not have permission to access this page.')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        operator_data = {
            "operator_name": request.form.get('operator_name'),
            "contact_name": request.form.get('contact_name'),
            "email": request.form.get('email'),
            "phone": request.form.get('phone'),
            "address": request.form.get('address')
        }

        if OperatorController.update_operator(operator_id, **operator_data):
            flash('Operator updated successfully.')
            return redirect(url_for('operators_list'))
        else:
            flash('Failed to update operator.')
            return redirect(url_for('edit_operator', operator_id=operator_id))

    operator_details = OperatorController.get_operator_details(operator_id)
    if operator_details:
        return render_template('operators/edit_operator.html', operator=operator_details)
    else:
        flash('Operator not found.')
        return redirect(url_for('operators_list'))
    
@app.route('/tours_for_operator/<int:operator_id>')
def tours_for_operator(operator_id):
    if not is_logged_in():
        flash('You must be logged in to access this page.')
        return redirect(url_for('login'))
    elif not is_admin():
        flash('You do not have permission to access this page.')
        return redirect(url_for('dashboard'))
    # You might want to check if the user is logged in or has the right permissions
    print(operator_id)
    tours = OperatorController.get_tours_by_operator(operator_id)
    if not tours:
        flash('No tours found for this operator.')
    return render_template('operators/tours_for_operator.html', tours=tours, operator_id=operator_id)

@app.route('/add_operator', methods=['GET', 'POST'])
def add_operator():
    if request.method == 'POST':
        operator_name = request.form['operator_name']
        contact_name = request.form['contact_name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
   
        if OperatorController.add_operator(operator_name, contact_name, email, phone, address):
            flash('Operator added successfully')
            return redirect(url_for('operators_list'))
        else:
            flash('Failed to add operator')
    operators=OperatorController.get_all_operators()
    return render_template('operators/add_operator.html', operators=operators)


