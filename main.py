import requests
import json
import time

from card import Card
from card import CardEncoder



api_url = 'https://api.fabdb.net'
cards_uri = '/cards'
#response = requests.get(api_url)
response = requests.get(api_url + cards_uri + '/UPR000')
#print(response.json())
json_dict = response.json()
#cardData = json.loads(response.json())
cardData = Card(json_dict["identifier"], json_dict["rarity"], json_dict["keywords"], json_dict["stats"])
print(vars(cardData))

cardList = []
# UPR000 - UPR223
for i in range(224):
    cardid = f'/UPR{i:03d}'
    response = requests.get(api_url + cards_uri + cardid)    
    json_dict = response.json()
    cardList.append(Card(json_dict["identifier"], json_dict["rarity"], json_dict["keywords"], json_dict["stats"]))
    print('added ' + cardid)
    time.sleep(1)

f = open("cards.json", "w")
f.write(json.dumps(cardList, cls=CardEncoder))
f.close()