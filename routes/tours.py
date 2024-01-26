from flask import render_template, redirect, url_for, request
from app import app
from controller.tour_controllers import TourController


@app.route('/tours')
def tours():
    all_tours = TourController.get_all_tours()
    return render_template('tours.html', tours=all_tours)

