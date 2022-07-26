from json import JSONEncoder

class Card:
    def __init__(self, identifier, rarity, keywords, stats, image_url):
        self.identifier = identifier
        self.rarity = rarity
        self.keywords = keywords
        self.stats = stats
        self.image_url = image_url
        self.image = None

class Pack:
    def __init__(self, cards):
        self.cards = cards

# subclass JSONEncoder
class CardEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__