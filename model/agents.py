
from model.db import database_execute_action, database_execute_lastrowid, database_execute_query_fetchone, database_execute_query_fetchall

class Agents:
    # def __init__(self, user_id, first_name, last_name, email, phone, wechat, agency_name):
    #     self._agent_id = None
    #     self._user_id = user_id
    #     self._first_name = first_name
    #     self._last_name = last_name
    #     self._email = email
    #     self._phone = phone
    #     self._wechat = wechat
    #     self._agency_name = agency_name
    # @property
    # def agent_id(self):
    #     return self._agent_id
    # @property
    # def user_id(self):
    #     return self._user_id
    # @property
    # def first_name(self):
    #     return self._first_name
    # @property
    # def last_name(self):
    #     return self._last_name
    # @property
    # def email(self):
    #     return self._email
    # @property
    # def phone(self):
    #     return self._phone
    # @property
    # def wechat(self):
    #     return self._wechat
    # @property
    # def agency_name(self):
    #     return self._agency_name
    # @agent_id.setter
    # def agent_id(self, value):
    #     self._agent_id = value
    # @user_id.setter
    # def user_id(self, value):
    #     self._user_id = value
    # @first_name.setter
    # def first_name(self, value):
    #     self._first_name = value
    # @last_name.setter
    # def last_name(self, value):
    #     self._last_name = value
    # @email.setter
    # def email(self, value):
    #     self._email = value
    # @phone.setter
    # def phone(self, value):
    #     self._phone = value
    # @wechat.setter
    # def wechat(self, value):
    #     self._wechat = value
    # @agency_name.setter
    # def agency_name(self, value):
    #     self._agency_name = value

    @staticmethod
    def add_agent(user_id,first_name, last_name, email, phone, wechat, agency_name ):
        query = """
            INSERT INTO Agents (UserID,FirstName, LastName, Email, Phone, Wechat, AgencyName)
            VALUES (%s,%s, %s, %s, %s, %s, %s);
        """
        # Execute the query
        return database_execute_action(query, (user_id,first_name, last_name, email, phone, wechat, agency_name))
    

    @staticmethod
    def get_all_agents():
        query = "SELECT * FROM Agents ORDER BY LastName ASC, FirstName ASC"
        return database_execute_query_fetchall(query)
    @staticmethod
    def get_agent_id_by_user_id(user_id):
        query = "SELECT AgentID FROM Agents WHERE UserID = %s"
        return database_execute_query_fetchone(query, (user_id,))
    
    @staticmethod
    def get_agent_details(agent_id):
        query = "SELECT * FROM Agents WHERE AgentID = %s"
        return database_execute_query_fetchone(query, (agent_id,))

    @staticmethod
    def update_agent(agent_id,first_name, last_name, email, phone, wechat, agency_name):
        query = """
            UPDATE Agents
            SET FirstName = %s, LastName = %s, Email = %s, Phone = %s, Wechat = %s, AgencyName= %s
            WHERE AgentID = %s
        """
        return database_execute_action(query, (first_name, last_name, email, phone, wechat, agency_name, agent_id))
    @staticmethod
    def get_agent_id_by_user_id(user_id):
        query = "SELECT AgentID FROM Agents WHERE UserID = %s"
        return database_execute_query_fetchone(query, (user_id,))