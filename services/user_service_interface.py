import abc

class UserServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_user(self, id, name, is_admin):
        pass