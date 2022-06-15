from json import JSONEncoder

class Card:
    def __init__(self, identifier, rarity, keywords, stats):
        self.identifier = identifier
        self.rarity = rarity
        self.keywords = keywords
        self.stats = stats

# subclass JSONEncoder
class CardEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__