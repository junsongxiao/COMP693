# model/auth.py

from flask import session
import bcrypt
# from model.users import Users
from controller.user_controllers import UserController
from model.db import database_execute_lastrowid, database_execute_query_fetchone, database_execute_action

class Auth:
    @staticmethod
    def log_out():
        session.clear()

    @staticmethod
    def log_in(username, password):
        user = UserController.get_user_by_username(username)
        if user and bcrypt.checkpw(password.encode("utf-8"), user["PasswordHash"].encode("utf-8")):
            session["UserID"] = user["UserID"]
            session["Username"] = user["Username"]
            session["Type"] = user["Type"]
            return True
        return False
    
    @staticmethod
    def create_user(username, password):
        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")

        # SQL query to insert a new user
        query = "INSERT INTO Users (Username, PasswordHash, Type) VALUES (%s, %s, %s);"
        values = (username, hashed_password, 'Customer')  # Assuming 'Customer' as default user type

        # Execute query and return the UserID
        return database_execute_lastrowid(query, values)

    

    
