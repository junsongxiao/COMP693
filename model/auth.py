from flask import session
import bcrypt
from model.db import get_cursor
# import model.user


"""
This module contains functions for authenticating users, and generally anything to do with hashing passwords.
This module should be used for all authentication, and the model.user module should be used for all other user-related tasks.
i.e. don't use bcrypt anywhere else.
"""

def log_in(username, password):
    """Attempt to login the user, return True if successful, False otherwise,
    and set the session variables"""
    user = model.user.get_user_by_username(username)
    if user is None:
        return False
    if bcrypt.checkpw(password.encode("utf-8"), user["hash"].encode("utf-8")):
        session["user_id"] = user["user_id"]
        session["username"] = user["username"]
        session["role"] = user["role"]

        if user["admin_id"]:
            session["admin_id"] = user["admin_id"]
        if user["doctor_id"]:
            session["doctor_id"] = user["doctor_id"]
        if user["nurse_id"]:
            session["nurse_id"] = user["nurse_id"]
        if user["patient_id"]:
            session["patient_id"] = user["patient_id"]
        if user["receptionist_id"]:
            session["receptionist_id"] = user["receptionist_id"]

        return True
    else:
        return False

def add_user(username,password,role,admin_id=None,doctor_id=None,nurse_id=None,patient_id=None,receptionist_id=None):
    """Add a new user to the database"""
    hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode(
        "utf-8"
    )
    query_string = """
    INSERT INTO user (username, hash, role, admin_id, doctor_id, nurse_id, patient_id, receptionist_id)
    VALUES (%(username)s, %(hash)s, %(role)s, %(admin_id)s, %(doctor_id)s, %(nurse_id)s, %(patient_id)s, %(receptionist_id)s)
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

