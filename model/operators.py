from model.db import database_execute_lastrowid, database_execute_query_fetchall, database_execute_action, database_execute_query_fetchone
class Operators:
    def __init__(self, operator_name, contact_name, email, phone, address):
        self._operator_id = None
        self._operator_name = operator_name
        self._contact_name = contact_name
        self._email = email
        self._phone = phone
        self._address = address
    @property
    def operator_id(self):
        return self._operator_id
    @property
    def operator_name(self):
        return self._operator_name
    @property
    def contact_name(self):
        return self._contact_name
    @property
    def email(self):
        return self._email
    @property
    def phone(self):
        return self._phone
    @property
    def address(self):
        return self._address
    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @email.setter
    def email(self, value):
        self._email = value
    @phone.setter
    def phone(self, value):
        self._phone = value
    @address.setter
    def address(self, value):
        self._address = value

    @staticmethod
    def get_operator_details(operator_id):
        query = "SELECT * FROM Operators WHERE OperatorID = %s"
        return database_execute_query_fetchone(query, (operator_id,))

    @staticmethod
    def update_operator(operator_id, operator_name, contact_name, email, phone, address):
        query = """
            UPDATE Operators
            SET OperatorName = %s, ContactName = %s, Email = %s, 
                Phone = %s, Address = %s
            WHERE OperatorID = %s
        """
        params = (operator_name, contact_name, email, phone, address, operator_id)
        return database_execute_action(query, params)
    
    @staticmethod
    def get_all_operators():
        query = "SELECT * FROM Operators"
        return database_execute_query_fetchall(query)
    
    @staticmethod
    def add_operator(operator_name, contact_name, email, phone, address):
        query = """
            INSERT INTO Operators (OperatorName, ContactName, Email, Phone, Address)
            VALUES (%s, %s, %s, %s, %s)
        """
        return database_execute_action(query)
    
    
