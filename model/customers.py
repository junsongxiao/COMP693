from model.db import database_execute_query_fetchall, database_execute_query_fetchone, database_execute_action, database_execute_lastrowid

class Customers:
    def __init__(self, user_id, first_name, last_name, email, phone, wechat, preferences, notes):
        self._customer_id = None
        self._user_id = user_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._wechat = wechat
        self._preferences = preferences
        self._notes = notes

    ##getters
    @property
    def customer_id(self):
        return self._customer_id
    @property
    def user_id(self):
        return self._user_id
    @property
    def first_name(self):
        return self._first_name
    @property
    def last_name(self):
        return self._last_name
    @property
    def email(self):
        return self._email
    @property
    def phone(self):
        return self._phone
    @property
    def wechat(self):
        return self._wechat
    @property
    def preferences(self):
        return self._preferences
    @property
    def notes(self):
        return self._notes
    
    ##setters
    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @first_name.setter
    def first_name(self, value):
        self._first_name = value
    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    @email.setter
    def email(self, value):
        self._email = value
    @phone.setter
    def phone(self, value):
        self._phone = value
    @wechat.setter
    def wechat(self, value):
        self._wechat = value
    @preferences.setter
    def preferences(self, value):
        self._preferences = value
    @notes.setter
    def notes(self, value):
        self._notes = value


    @staticmethod
    def get_all_customers():
        
        query = "SELECT * FROM Customers ORDER BY LastName ASC, FirstName ASC"
        return database_execute_query_fetchall(query)
    
    @staticmethod
    def get_customer_details(customer_id):
        query = "SELECT * FROM Customers WHERE CustomerID = %s"
        return database_execute_query_fetchone(query, (customer_id,))

    @staticmethod
    def update_customer(customer_id, first_name, last_name, email, phone, wechat, preferences, notes):
        # Update query with necessary fields
        query = "UPDATE Customers SET FirstName = %s, LastName = %s, Email = %s, Phone=%s, Wechat=%s, Preferences=%s, Notes=%s WHERE CustomerID = %s"
        return database_execute_action(query, (first_name, last_name, email, phone, wechat, preferences, notes, customer_id))
    
    @staticmethod
    def add_customer(first_name, last_name, email, phone, wechat, preferences, notes):
        query = """
            INSERT INTO Customers (FirstName, LastName, Email, Phone, Wechat, Preferences, Notes)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        # Execute the query
        return database_execute_action(query, (first_name, last_name, email, phone, wechat, preferences,notes))

