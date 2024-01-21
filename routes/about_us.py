from flask import redirect, url_for,render_template
from app import app

@app.route('/about_us')
def about_us():
    return render_template('general/about_us.html')  # or your appropriate logic here
