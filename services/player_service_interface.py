import abc

class PlayerServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_player(self, id, name, type):
        pass