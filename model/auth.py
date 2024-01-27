# model/auth.py

from flask import session
import bcrypt
from model.users import Users

class Auth:
    @staticmethod
    def log_out():
        session.clear()

    @staticmethod
    def log_in(username, password):
        user = Users.get_user_by_username(username)
        if user and bcrypt.checkpw(password.encode("utf-8"), user["PasswordHash"].encode("utf-8")):
            session["UserID"] = user["UserID"]
            session["Username"] = user["Username"]
            session["Type"] = user["Type"]
            return True
        return False
    
    @staticmethod
    def is_logged_in():
        return 'UserID' in session
