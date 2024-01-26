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




@app.route("/home", methods=["GET", "POST"])
def home():
    
    return render_template("general/home.html")

@app.route("/teams", methods=["GET", "POST"])
def teams():
    
    teams=[]
    doctors = model.doctor.get_all_doctors()
    nurses = model.nurse.get_all_nurses()
    receptionists = model.receptionist.get_all_receptionists()
    admins = model.admin.get_all_admins()
    

    for doctor in doctors:
        teams.append({"role": "Doctor", "name": doctor["first_name"] +" "+ doctor["last_name"],  "photo": doctor["photo"], "id": doctor["doctor_id"] })

    for nurse in nurses:
        teams.append({"role": "Nurse", "name": nurse["first_name"] +" "+ nurse["last_name"], "photo": nurse["photo"], "id": None})

    for admin in admins:

#         teams.append({"role": "Admin", "name": admin["first_name"] +" "+ admin["last_name"], "photo": "/images/default-avatar.jpg", "id": None})

#     for receptionist in receptionists:
#         teams.append({"role": "Receptionist", "name": receptionist["first_name"] +" "+ receptionist["last_name"], "photo": "/images/default-avatar.jpg", "id": None})

        teams.append({"role": "Admin", "name": admin["first_name"] +" "+ admin["last_name"], "photo": admin["photo"]})

    for receptionist in receptionists:
        teams.append({"role": "Receptionist", "name": receptionist["first_name"] +" "+ receptionist["last_name"], "photo": receptionist["photo"]})




    return render_template("general/our_team.html", teams=teams)

@app.route("/about_us", methods=["GET", "POST"])
def about_us():
    
    return render_template("general/about_us.html")

@app.route("/doctor_bio/<int:doctor_id>", methods=["GET", "POST"])
def doctor_bio(doctor_id):
    doctor=model.doctor.get_doctor_by_id(doctor_id)
    return render_template("general/doctor_bio.html", doctor=doctor)