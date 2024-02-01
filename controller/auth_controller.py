# controller/auth_controller.py

from model.auth import Auth

from controller.user_controllers import UserController
import bcrypt


class AuthController:
    @staticmethod
    def log_in(username, password):
        return Auth.log_in(username, password)
    
    @staticmethod
    def log_out():
        return Auth.log_out()

    @staticmethod
    def register_user(username, password, user_type):
        return UserController.add_user(username, password, user_type)
    
    @staticmethod
    def update_password(username, new_password):
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")
        return UserController.update_password(username, hashed_password)


