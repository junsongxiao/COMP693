
from model.db import database_execute_action, database_execute_lastrowid, database_execute_query_fetchone

class Users:
    def __init__(self, username, password_hash, user_type):
        self._user_id = None
        self._username = username
        self._password_hash = password_hash
        self._type = user_type

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if self._user_id is None:
            self._user_id = value
        else:
            raise ValueError("User ID can only be set once.")

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, value):
        self._password_hash = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    
    """
    This module contains functions for interacting with the USER table in the database.
    Note: Password hashes are never returned by these functions for security reasons.
        All authentication should be done through the model.auth module.
    """
    @staticmethod
    def update_password(username, new_hashed_password):
        query = "UPDATE Users SET PasswordHash = %s WHERE Username = %s"
        return database_execute_action(query, (new_hashed_password, username))
    
    @staticmethod
    def get_user_by_id(user_id):
        query = "SELECT * FROM Users WHERE UserID = %s"
        return database_execute_query_fetchone(query, (user_id,))
    @staticmethod
    def get_user_by_username(username):
        query = "SELECT * FROM Users WHERE Username = %s"
        try:
            return database_execute_query_fetchone(query, (username,))
        except Exception as e:
            print(f"Error fetching user by username: {e}")
            return None
    @staticmethod
    def get_user_role_details(user_id):
        query = """
        SELECT role, title, first_name, last_name
        FROM Users
        JOIN Customers ON Users.UserID = Customers.UserID
        WHERE Users.UserID = %s;
        """
        user = database_execute_query_fetchone(query, (user_id,))
        if user:
            return user['role'], user
        return None, None

    @staticmethod
    def update_user(user_id, first_name, last_name, email, phone, wechat, preferences, notes):
        query = """
            UPDATE Users
            SET FirstName = %s, LastName = %s, Email = %s, Phone = %s, Wechat = %s, Preferences = %s, Notes = %s
            WHERE UserID = %s
        """
        return database_execute_action(query, (first_name, last_name, email, phone, wechat, preferences, notes, user_id))

    # def get_all_users():
    #     """Returns a list of all users."""
    #     query_string = """
    #     SELECT *
    #     FROM users
    #     """
    #     connection = get_cursor()
    #     connection.execute(query_string)
    #     return connection.fetchall()


    # def get_user_by_username(username):
    #     """Returns a user by their username."""
    #     query_string = """
    #     SELECT *
    #     FROM users
    #     WHERE username = %(username)s;
    #     """
    #     connection = get_cursor()
    #     connection.execute(
    #         query_string,
    #         {"username": username},
    #     )
    #     return connection.fetchone()


    # def get_user_by_id(user_id):
    #     """Returns a user by their user_id."""
    #     query_string = """
    #     SELECT *
    #     FROM user
    #     WHERE user_id = %(user_id)s;
    #     """
    #     connection = get_cursor()
    #     connection.execute(
    #         query_string,
    #         {"user_id": user_id},
    #     )
    #     return connection.fetchone()

    # def get_user_by_id(user_id):
    #     """Returns a user by their user_id."""
    #     query_string = """
    #     SELECT user.*, details.first_name, details.last_name
    #     FROM user
    #     LEFT JOIN (
    #         SELECT 'admin' as role, admin_id as id, first_name, last_name FROM administrator
    #         UNION ALL
    #         SELECT 'doctor' as role, doctor_id as id, first_name, last_name FROM doctor
    #         UNION ALL
    #         SELECT 'nurse' as role, nurse_id as id, first_name, last_name FROM nurse
    #         UNION ALL
    #         SELECT 'patient' as role, patient_id as id, first_name, last_name FROM patient
    #         UNION ALL
    #         SELECT 'receptionist' as role, receptionist_id as id, first_name, last_name FROM receptionist
    #     ) as details ON user.role = details.role AND user.user_id = details.id
    #     WHERE user.user_id = %(user_id)s;
    #     """
        
    #     connection = get_cursor()
    #     connection.execute(
    #         query_string,
    #         {"user_id": user_id},
    #     )
    #     return connection.fetchone()


    # def get_user_by_role_id(role, role_id):
    #     """Returns a user by their role_id."""
    #     query_string = """
    #     SELECT *
    #     FROM user
    #     WHERE role = %(role)s
    #     AND (admin_id = %(role_id)s
    #     OR doctor_id = %(role_id)s
    #     OR nurse_id = %(role_id)s
    #     OR patient_id = %(role_id)s
    #     OR receptionist_id = %(role_id)s);
    #     """
    #     connection = get_cursor()
    #     connection.execute(
    #         query_string,
    #         {"role_id": role_id,
    #         "role": role},
    #     )
    #     return connection.fetchone()

    # def get_user_role_details(user_id):
    #     """Returns a tuple of the user's role and the details of that role."""
    #     query_string = """
    #     SELECT role, admin_id, doctor_id, nurse_id, patient_id, receptionist_id
    #     FROM user
    #     WHERE user_id = %(user_id)s;
    #     """
    #     connection = get_cursor()
    #     connection.execute(
    #         query_string,
    #         {"user_id": user_id},
    #     )
    #     user = connection.fetchone()
    #     role = user["role"]
    #     match role:
    #         case "admin":
    #             return (role, get_admin_by_id(user["admin_id"]))
    #         case "doctor":
    #             return (role, get_doctor_by_id(user["doctor_id"]))
    #         case "nurse":
    #             return (role, get_nurse_by_id(user["nurse_id"]))
    #         case "patient":
    #             return (role, get_patient_by_id(user["patient_id"]))
    #         case "receptionist":
    #             return (role, get_receptionist_by_id(user["receptionist_id"]))
    #         case _:
    #             return (None, None)
            

    # def delete_user(user_id):
    #     """Deletes a user by their user ID."""
    #     query_string = """
    #     DELETE FROM user
    #     WHERE user_id = %(user_id)s;
    #     """
    #     connection = get_cursor()
    #     connection.execute(query_string, {"user_id": user_id})
    #     connection.commit()

