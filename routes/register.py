from flask import render_template, request, redirect, url_for, session, flash
from app import app

import model.auth

from routes.session_utils import is_logged_in


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Registers a new user
    Note: Only patients can register themselves, others must be added by an admin
    """
    # Redirect to index if the user is already logged in
    if is_logged_in():
        return redirect(url_for("index"))
    
    # Fetch the list of doctors
    doctors = model.doctor.get_all_doctors()

    # If the request method is POST, register the new user
    if request.method == "POST":
        # Check if the username is already taken
        existing_patient = model.user.get_user_by_username(request.form.get("username"))
        if existing_patient:
            error_msg = "Username already taken. Please choose a different username."
            return render_template("auth/register.html", error_msg=error_msg, doctors=doctors)

        # Check if the email is already taken
        existing_patient = model.patient.get_patient_by_email(request.form.get("email"))
        if existing_patient:
            error_msg = "Email already taken. Please choose a different email."
            return render_template("auth/register.html", error_msg=error_msg, doctors=doctors)
        
        # Check if the password and confirm password match
        if request.form.get("password") != request.form.get("confirm_password"):
            error_msg = "Passwords do not match. Please enter again."
            return render_template("auth/register.html", error_msg=error_msg, doctors=doctors)

        # If the user chooses to automatically assign a doctor
        if request.form.get("health_professional") == "auto":
            # Find the doctor with the least number of patients
            assigned_doctor = model.doctor.get_doctor_with_least_patients()

            # If a doctor is found, use their ID; otherwise, set it to None
            doctor_id = assigned_doctor['doctor_id'] if assigned_doctor else None
        else:
            # Use the selected doctor's ID
            doctor_id = request.form.get("health_professional")

        # Add the new patient
        patient_id = model.patient.create_patient(
            request.form.get("title"),
            request.form.get("first_name"),
            request.form.get("last_name"),
            request.form.get("dob"),
            request.form.get("phone_number"),
            request.form.get("street_address"),
            request.form.get("suburb"),
            request.form.get("city"),
            request.form.get("postcode"),
            request.form.get("email"),
            doctor_id,
        )

        # Create the new user
        if patient_id and model.auth.add_user(
            request.form.get("username"),
            request.form.get("password"),
            "patient",
            patient_id=patient_id,
        ):
            # Set the success message
            success_msg = "Registration successful. You can now log in."
            # Use flash to display the message on the next redirected page (login)
            flash(success_msg)
            # Registration successful, redirect to login page
            return render_template("auth/login.html", success_msg=success_msg)
        else:
            error_msg = "Registration failed. Please try again."
            return render_template("auth/register.html", error_msg=error_msg, doctors=doctors)
    # If the request method is GET, display the registration form
    else:
        return render_template("auth/register.html", doctors=doctors)
