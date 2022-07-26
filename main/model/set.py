from json import JSONEncoder

class Set:
    def __init__(self, cards):
        self.cards = cards

# subclass JSONEncoder
class CardEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__