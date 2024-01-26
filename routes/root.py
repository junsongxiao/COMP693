from flask import redirect, url_for,render_template
from app import app

"""
This module contains the route for the root page.
Note: All users can view the root, but we still use auth_handler to ensure the user is logged in
"""

@app.route("/")
def home():
    # return redirect(url_for("home"))
    print("route rendered")
    return render_template("general/home.html")
