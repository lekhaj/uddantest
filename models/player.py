from enum import Enum

class Player(object):
    def __init__(self, id, name, type):
        self.player_id = id
        self.name = name
        self.type = type
        self.credit_worth = 0
        self.points = 0

class PlayerType(Enum):
    BATSMAN, BOWLER, KEEPER = 1, 2, 3 #all rounder logic will add later