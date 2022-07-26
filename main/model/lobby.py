from opcode import hasconst
from uuid import uuid4
from json import JSONEncoder
import json

from main.model.player import PlayerEncoder

class Lobby:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.gameid = str(uuid4())

    def AddPlayer(self, Player):
        self.players.append(Player)

class LobbyEncoder(JSONEncoder):
    def default(self, o):
        if hasattr(o, 'reprJSON'):
            return o.reprJSON()
        else:
            return o.__dict__

