from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

from flask_mail import Mail, Message

from routes.chat import chat_bp

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

app.register_blueprint(chat_bp)

import routes.root  # Root page route
import routes.session_utils  # Session utility routes
import routes.general
import routes.auth  # Authentication routes (login/logout)
import routes.operators
import routes.customers
import routes.agents
import routes.quotes
import routes.user
import routes.tours
import routes.inquiries
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