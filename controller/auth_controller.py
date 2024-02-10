# controller/auth_controller.py

from model.auth import Auth

from controller.user_controllers import UserController
from controller.customer_controllers import CustomerController
import bcrypt


class AuthController:
    @staticmethod
    def log_in(username, password):
        return Auth.log_in(username, password)
    
    @staticmethod
    def log_out():
        return Auth.log_out()

    # @staticmethod
    # def register_user(username, password, user_type):
    #     return UserController.add_user(username, password, user_type)
    # In AuthController
    @staticmethod
    def register_user(username, password, first_name, last_name, email, phone, wechat):
        user_id = Auth.create_user(username, password)
        if user_id:
            customer_created =CustomerController.create_customer(user_id, first_name, last_name, email, phone, wechat,preferences=None,notes=None)
            if customer_created:
                return True
        return False

    @staticmethod
    def update_password(username, new_password):
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")
        return UserController.update_password(username, hashed_password)
    @staticmethod
    def create_user(username, password):
        return Auth.create_user(username, password)


