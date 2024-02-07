from flask import redirect, url_for,render_template, session
from app import app
from controller.tour_controllers import TourController

"""
This module contains the route for the root page.
Note: All users can view the root, but we still use auth_handler to ensure the user is logged in
"""

@app.route("/")
def index():
    tours=TourController.get_all_tours()
  
    return render_template("general/home.html", tours=tours)
