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
import model.auth





@app.route("/about_us", methods=["GET", "POST"])
def about_us():
    
    return render_template("general/about_us.html")

@app.route("/doctor_bio/<int:doctor_id>", methods=["GET", "POST"])
def doctor_bio(doctor_id):
    doctor=model.doctor.get_doctor_by_id(doctor_id)
    return render_template("general/doctor_bio.html", doctor=doctor)