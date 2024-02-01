

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mail import Mail, Message

import connect
# Import models and controllers here
# import model.users, model.bookings, model.tours, model.auth
# from model import users, bookings, tours,auth
# import controller.auth_controller, controller.user_controller, controller.booking_controller, controller.tour_controller
# from controller import user_controllers, booking_controllers,auth_controllers


app = Flask(__name__)

app.secret_key = 'secrete_key_for_secured_sessions'

mail = Mail(app)


app.config['MAIL_SERVER'] = 'smtp-relay.brevo.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'words4sammy@gmail.com'
app.config['MAIL_PASSWORD'] = 'xsmtpsib-fb53555f722e407bb8aac0a2b5bb1ad27e4c9ef3ef017187b1bf2a64aad33a9d-34OcgLQJSYWDv1FX'
app.config['MAIL_DEFAULT_SENDER'] = 'words4sammy@gmail.com'



### Routes ###

import routes.root  # Root page route
import routes.session_utils  # Session utility routes
import routes.general
import routes.auth  # Authentication routes (login/logout)
import routes.operators
import routes.tours
# import routes.inquire
import routes.dashboard
import routes.booking
# import routes.register  # register route
import routes.error  # Error handling routes
# import routes.about_us
# import routes.dashboard  # Dashboard route
import routes.user  # User routes
# import routes.booking  # Booking routes
# import routes.tour  # Tour routes
# import routes.payment  # Payment routes


##### Routes #####





if __name__ == "__main__":
    app.debug = True
    app.run()