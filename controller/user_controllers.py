from flask import session
from datetime import datetime,date
from model.db import database_execute_query_fetchone, database_execute_query_fetchall,database_execute_action,database_execute_lastrowid
from typing import List,Dict, Any, Optional
from flask import abort, session,flash
import model.users,model.bookings,model.agencies,model.customers,model.operators,model.payments,model.tours,model.utilities
import json
import mysql.connector
import sqlite3




class UserController:
    # User-related business logic and interactions with the user model
    pass
