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
# import model.auth





@app.route("/about_us", methods=["GET", "POST"])
def about_us():
    
    return render_template("general/about_us.html")
