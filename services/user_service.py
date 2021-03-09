from services.user_service_interface import UserServiceInterface
from models.user import User


class UserService(UserServiceInterface):
    user_details = {}

    def add_user(self,id, name, is_admin):
        user = User(id, name, is_admin)
        self.__class__.user_details[id] = user
        return user