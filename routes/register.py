from flask import render_template, request, redirect, url_for, session, flash
from app import app

import model.auth

from routes.session_utils import is_logged_in


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Registers a new user

    """
    # Redirect to index if the user is already logged in
    if is_logged_in():
        return redirect(url_for("home"))
    else:   
        return render_template("auth/register.html")
