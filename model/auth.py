from flask import session
import bcrypt
from model.users import Users

def log_in(username, password):
    user = Users.get_user_by_username(username)
    if user and bcrypt.checkpw(password.encode("utf-8"), user["PasswordHash"].encode("utf-8")):
        session["UserID"] = user["UserID"]
        session["Username"] = user["Username"]
        session["Type"] = user["Type"]
        return True
    return False



# from flask import session
# import bcrypt
# from model.db import get_cursor
# # import model.user


# """
# This module contains functions for authenticating users, and generally anything to do with hashing passwords.
# This module should be used for all authentication, and the model.user module should be used for all other user-related tasks.
# i.e. don't use bcrypt anywhere else.
# """

# def log_in(username, password):
#     """Attempt to login the user, return True if successful, False otherwise,
#     and set the session variables"""
#     user = model.user.get_user_by_username(username)
#     if user is None:
#         return False
#     if bcrypt.checkpw(password.encode("utf-8"), user["hash"].encode("utf-8")):
#         session["user_id"] = user["user_id"]
#         session["username"] = user["username"]
#         session["role"] = user["role"]

        

#         return True
#     else:
#         return False

# def add_user(username,password,role,):
#     """Add a new user to the database"""
#     hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode(
#         "utf-8"
#     )
#     query_string = """
#     INSERT INTO user (username, hash, role, admin_id, doctor_id, nurse_id, patient_id, receptionist_id)
#     VALUES (%(username)s, %(hash)s, %(role)s)
#     """
#     connection = get_cursor()
#     connection.execute(
#         query_string,
#         {
#             "username": username,
#             "hash": hash,
#             "role": role,

#         },
#     )
#     return connection.lastrowid


# def update_password(username, password):
#     """Update a user's password"""
#     hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode(
#         "utf-8"
#     )
#     query_string = """
#     UPDATE user SET
#     `hash` = %(hash_password)s
#     WHERE `username` = %(username)s;
#     """
#     connection = get_cursor()
#     connection.execute(
#         query_string,
#         {
#             "username": username,
#             "hash": hash,
#         },
#     )
#     if connection.rowcount == 1:
#         return True  # Update successful
#     else:
#         return False  # Update failed

