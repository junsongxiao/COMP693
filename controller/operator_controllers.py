from model.operators import Operators
from model.tours import Tours

class OperatorController:
    @staticmethod
    def get_operator_details(operator_id):
        return Operators.get_operator_details(operator_id)

    @staticmethod
    def update_operator(operator_id, operator_data):
        return Operators.update_operator(
            operator_id,
            operator_data['operator_name'],
            operator_data['contact_name'],
            operator_data['email'],
            operator_data['phone'],
            operator_data['address']
        )
    @staticmethod
    def get_all_operators():
        return Operators.get_all_operators()
    @staticmethod
    def get_tours_by_operator(operator_id):
        return Tours.get_tours_by_operator(operator_id)
    
    @staticmethod
    def add_operator(operator_name, contact_name, email, phone, address):
        return Operators.add_operator(operator_name, contact_name, email, phone, address)
