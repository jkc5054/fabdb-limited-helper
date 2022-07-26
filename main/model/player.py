from json import JSONEncoder

class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def reprJSON(self):
        return self.__dict__

class PlayerEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__