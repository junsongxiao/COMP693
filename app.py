

from flask import Flask, render_template, request, redirect, url_for, session, flash
import connect
# Import models and controllers here
# import model.users, model.bookings, model.tours, model.auth
# from model import users, bookings, tours,auth
# import controller.auth_controller, controller.user_controller, controller.booking_controller, controller.tour_controller
# from controller import user_controllers, booking_controllers,auth_controllers

app = Flask(__name__)
app.secret_key = 'secrete_key_for_secured_sessions'

### Routes ###

import routes.root  # Root page route
import routes.general
import routes.auth  # Authentication routes (login/logout)
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