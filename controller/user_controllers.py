from flask import session
from datetime import datetime,date
from model.users import Users
import bcrypt
# from model.db import database_execute_action, database_execute_lastrowid, database_execute_query_fetchone

from model.db import database_execute_query_fetchone, database_execute_query_fetchall,database_execute_action,database_execute_lastrowid
from typing import List,Dict, Any, Optional
from flask import abort, session,flash
import model.users,model.bookings,model.agencies,model.customers,model.operators,model.payments,model.tours,model.utilities
import json
import mysql.connector
import sqlite3




class UserController:


    @staticmethod
    def get_user_by_username(username):
        query = "SELECT * FROM Users WHERE Username = %s"
        user = database_execute_query_fetchone(query, (username,))
        return user

    # @staticmethod
    # def add_user(username, password, user_type):
    #     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")
    #     query = "INSERT INTO Users (Username, PasswordHash, Type) VALUES (%s, %s, %s)"
    #     user_id = database_execute_lastrowid(query, (username, hashed_password, user_type))
    #     return user_id
  
    @staticmethod
    def create_customer(user_id, first_name, last_name, email, phone, wechat):
        # SQL query to insert customer details
        query = """
            INSERT INTO Customers (UserID, FirstName, LastName, Email, Phone, Wechat)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        values = (user_id, first_name, last_name, email, phone, wechat)

        # Execute query and check if the customer was successfully added
        return database_execute_action(query, values)

    
    @staticmethod
    def delete_user(user_id):
        query = "DELETE FROM Users WHERE UserID = %s"
        return database_execute_action(query, (user_id,))
    
    @staticmethod
    def get_user_profile(user_id):
        return Users.get_user_by_id(user_id)

    @staticmethod
    def update_user_profile(user_id, first_name, last_name, email, phone, wechat, preferences, notes):
        return Users.update_user(user_id, first_name, last_name, email, phone, wechat, preferences, notes)
    
    # @staticmethod
    # def update_password(username, new_password):
    #     hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")
    #     query = "UPDATE Users SET PasswordHash = %s WHERE Username = %s"
    #     return database_execute_action(query, (hashed_password, username))
    
    @staticmethod
    def get_user_role_details(user_id):
        return Users.get_user_role_details(user_id)
