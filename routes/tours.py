from flask import render_template, redirect, url_for, request, flash
from app import app
from controller.tour_controllers import TourController


@app.route('/tours')
def tours():
    all_tours = TourController.get_all_tours()
    return render_template('tours/tours.html', tours=all_tours)
@app.route('/edit_tour/<int:tour_id>', methods=['GET', 'POST'])
def edit_tour(tour_id):
    if request.method == 'POST':
        # Extract form data
        tour_name = request.form['TourName']
        city = request.form['City']
        region = request.form['Region']
        description = request.form['TourDescription']
        adult_price = request.form['AdultPrice']
        child_price = request.form['ChildPrice']
        infant_price = request.form['InfantPrice']
        family_price = request.form['FamilyPrice']
        tour_time = request.form['TourTime']
        report_time = request.form['ReportTime']
        terms = request.form['Terms']
        reporting_add = request.form['ReportingAdd']
        tour_add = request.form['TourAdd']
        commission_rate = request.form['CommissionRate']

        if TourController.update_tour(tour_id, tour_name, city, region, description, adult_price, 
                                      child_price, infant_price, family_price, tour_time, report_time,
                                      terms, reporting_add, tour_add, commission_rate):
            flash('Tour updated successfully.')
        else:
            flash('Failed to update tour.')

        return redirect(url_for('view_tours'))

    tour = TourController.get_tour_details(tour_id)
    return render_template('edit_tour.html', tour=tour)

@app.route('/add_tour', methods=['GET', 'POST'])
def add_tour():
    if request.method == 'POST':
        # Extract form data
        tour_name = request.form.get('tour_name')
        operator_id = request.form.get('operator_id')
        # Add other fields as necessary

        # Add new tour
        if TourController.add_tour(tour_name, operator_id):
            flash('New tour added successfully.')
            return redirect(url_for('tour_list'))  # Redirect to tour list or appropriate page
        else:
            flash('Failed to add new tour.')
            return redirect(url_for('add_tour'))

    return render_template('tours/add_tour.html')

@app.route('/add_tour', methods=['GET', 'POST'])
def add_tour():
    if request.method == 'POST':
        # Extract form data from the request
        operator_id = request.form.get('operator_id')
        tour_name = request.form.get('tour_name')
        city = request.form.get('city')
        region = request.form.get('region')
        description = request.form.get('description')
        adult_price = request.form.get('adult_price')
        child_price = request.form.get('child_price')
        infant_price = request.form.get('infant_price')
        family_price = request.form.get('family_price')
        tour_time = request.form.get('tour_time')
        report_time = request.form.get('report_time')
        terms = request.form.get('terms')
        reporting_add = request.form.get('reporting_add')
        tour_add = request.form.get('tour_add')
        commission_rate = request.form.get('commission_rate')

        

        # Invoke the controller method
        if TourController.add_tour(operator_id, tour_name, city, region, description, adult_price, child_price, infant_price, family_price, tour_time, report_time, terms, reporting_add, tour_add, commission_rate):
            flash('New tour added successfully.')
            return redirect(url_for('tour_list'))
        else:
            flash('Failed to add new tour.')
    
    return render_template('tours/add_tour.html')




