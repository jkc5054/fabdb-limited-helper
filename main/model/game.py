from json import JSONEncoder
from uuid import uuid4
from random import shuffle
from main.model.pack import Pack
import json

class Game:
    def __init__(self, name, players):
        self.name = name
        self.packs = []
        for x in range(8):
            p = Pack()
            p.generate_pack()
            self.packs.append(p)
        shuffle(players)
        self.players = players
        self.gameid = str(uuid4())

class GameEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__