from flask import session
from datetime import datetime,date
from model.users import Users
from model.customers import Customers
import bcrypt
# from model.db import database_execute_action, database_execute_lastrowid, database_execute_query_fetchone

from model.db import database_execute_query_fetchone, database_execute_query_fetchall,database_execute_action,database_execute_lastrowid
from typing import List,Dict, Any, Optional
from flask import abort, session,flash
import model.users,model.bookings,model.agents,model.customers,model.operators,model.payments,model.tours,model.utilities
import json
import mysql.connector
import sqlite3




class UserController:


    @staticmethod
    def get_user_by_username(username):
        # Users.get_user_by_username(username)
        query = "SELECT * FROM Users WHERE Username = %s"
        user = database_execute_query_fetchone(query, (username,))
        return user

    # @staticmethod
    # def add_user(username, password, user_type):
    #     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")
    #     query = "INSERT INTO Users (Username, PasswordHash, Type) VALUES (%s, %s, %s)"
    #     user_id = database_execute_lastrowid(query, (username, hashed_password, user_type))
    #     return user_id
    
    
        
    # @staticmethod
    # def create_customer(user_id, first_name, last_name, email, phone, wechat, preferences, notes):
    #     if preferences is None:
    #         preferences = ""
    #     if notes is None:
    #         notes = ""
    #     # SQL query to insert customer details
    #     query = """
    #         INSERT INTO Customers (UserID, FirstName, LastName, Email, Phone, Wechat, Preferences, Notes)
    #         VALUES (%s, %s, %s, %s, %s, %s);
    #     """
    #     values = (user_id, first_name, last_name, email, phone, wechat, preferences, notes)

    #     # Execute query and check if the customer was successfully added
    #     return database_execute_action(query, values)
    @staticmethod
    def get_all_users():
        return Users.get_all_users()
    @staticmethod
    def get_user_by_id(user_id):
        return Users.get_user_by_id(user_id)
    
    # @staticmethod
    # def update_user(user_id,user_name,user_type):
    #     return Users.update_user(user_id,user_name,user_type)
    @staticmethod
    def update_user(user_id, username):
        return Users.update_user(user_id, username)
    

    @staticmethod
    def get_profile_details(user_id, user_type):
        return Users.get_profile_details(user_id, user_type)

    @staticmethod
    def update_customer_profile(user_id, first_name, last_name, email, phone, wechat,preferences,notes):
        return Users.update_customer_profile(user_id, first_name, last_name, email, phone, wechat,preferences,notes)
    
    @staticmethod
    def update_agent_profile(user_id, first_name, last_name, email, phone, wechat, agency_name):
        return Users.update_agent_profile(user_id, first_name, last_name, email, phone, wechat,agency_name)

    @staticmethod
    def update_admin_profile(user_id, first_name, last_name, email, phone, wechat):
        return Users.update_admin_profile(user_id, first_name, last_name, email, phone, wechat)

    
    @staticmethod
    def delete_user(user_id):
        query = "DELETE FROM Users WHERE UserID = %s"
        return database_execute_action(query, (user_id,))
    
    # @staticmethod
    # def get_user_profile(user_id, user_type):
    #     # return Users.get_user_by_id(user_id)
    #     return Users.get_profile_details(user_id, user_type)

    # @staticmethod
    # def update_user_profile(user_id, first_name, last_name, email, phone, wechat, preferences, notes):
    #     return Users.update_user(user_id, first_name, last_name, email, phone, wechat, preferences, notes)
    
    @staticmethod
    def update_password(user_id,new_password):
        return Users.update_password(user_id,new_password)
    @staticmethod
    def update_type(user_id,user_type):
        return Users.update_type(user_id,user_type)
    @staticmethod
    def add_user(username, password, user_type):
        return Users.add_user(username, password, user_type)
    @staticmethod
    def create_login_for_customer(customer_id,user_id):
        return Users.create_login_for_customer(customer_id,user_id)
    @staticmethod
    def create_login_for_agent(agent_id,user_id):
        return Users.create_login_for_agent(agent_id,user_id)
    # @staticmethod
    # def update_password(username, new_password):
    #     hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")
    #     query = "UPDATE Users SET PasswordHash = %s WHERE Username = %s"
    #     return database_execute_action(query, (hashed_password, username))
    
    # @staticmethod
    # def get_user_role_details(user_id):
    #     return Users.get_user_role_details(user_id)
    @staticmethod
    def get_customer_profile(user_id):
        return Users.get_customer_by_user_id(user_id)
    @staticmethod
    def get_agent_profile(user_id):
        return Users.get_agent_by_user_id(user_id)
    @staticmethod
    def get_admin_profile(user_id):
        return Users.get_admin_by_user_id(user_id)
