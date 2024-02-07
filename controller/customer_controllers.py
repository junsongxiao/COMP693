from model.customers import Customers
class CustomerController:
    @staticmethod
    def get_all_customers():
        return Customers.get_all_customers()

    @staticmethod
    def get_customer_details(customer_id):
        return Customers.get_customer_details(customer_id)

    @staticmethod
    def update_customer(customer_id, first_name, last_name, email, phone, wechat, preferences, notes):
        return Customers.update_customer(customer_id, first_name, last_name, email, phone, wechat, preferences, notes)
    
    @staticmethod
    def add_customer(first_name, last_name, email, phone, wechat, preferences, notes):
        return Customers.add_customer(first_name, last_name, email, phone, wechat, preferences, notes)
    @staticmethod
    def get_customer_id_by_user_id(user_id):
        return Customers.get_customer_id_by_user_id(user_id)
    

