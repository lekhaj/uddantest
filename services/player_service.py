from services.player_service_interface import PlayerServiceInterface
from models.player import Player


class PlayerService(PlayerServiceInterface):
    player_details = {}

    def add_player(self, id, name, type):
        player = Player(id, name, type)
        self.__class__.player_details[id] = player
        return player