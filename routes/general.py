from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    abort
)
from app import app
from routes.session_utils import auth_handler
from controller.tour_controllers import TourController
# import model.auth


@app.route("/", methods=["GET", "POST"])
def home():
    tours=TourController.get_all_tours()
    return render_template("general/home.html", tours=tours)


@app.route("/about_us", methods=["GET", "POST"])
def about_us():
    
    return render_template("general/about_us.html")
