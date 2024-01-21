from flask import session
import bcrypt
from model.db import get_cursor
from model.users import get_user_by_username, get_user_by_id, get_all_users, update_password


class AuthController:
    @staticmethod
    def log_in(username, password):
        """Attempt to login the user, return True if successful, False otherwise,
        and set the session variables"""
        # user = model.user.get_user_by_username(username)
        user = get_user_by_username(username)   
        if user is None:
            return False
        if bcrypt.checkpw(password.encode("utf-8"), user["hash"].encode("utf-8")):
            session["UserID"] = user["UserID"]
            session["Username"] = user["Username"]
            session["Type"] = user["Type"]

           

            return True
        else:
            return False

    def add_user(username,password,role):
        """Add a new user to the database"""
        hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode(
            "utf-8"
        )
        query_string = """
        INSERT INTO user (username,PasswordHash, Type)
        VALUES (%(username)s, %(hash)s, %(role)s)
        """
        connection = get_cursor()
        connection.execute(
            query_string,
            {
                "username": username,
                "hash": hash,
                "role": role,
                "admin_id": admin_id,
                "doctor_id": doctor_id,
                "nurse_id": nurse_id,
                "patient_id": patient_id,
                "receptionist_id": receptionist_id,
            },
        )
        return connection.lastrowid


    def update_password(username, password):
        """Update a user's password"""
        hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode(
            "utf-8"
        )
        query_string = """
        UPDATE user SET
        `hash` = %(hash_password)s
        WHERE `username` = %(username)s;
        """
        connection = get_cursor()
        connection.execute(
            query_string,
            {
                "username": username,
                "hash": hash,
            },
        )
        if connection.rowcount == 1:
            return True  # Update successful
        else:
            return False  # Update failed

