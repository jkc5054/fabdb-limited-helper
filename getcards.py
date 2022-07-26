import requests
import shutil
import json
import time
import jsonpickle

from main.model.card import Card
from main.model.card import CardEncoder



api_url = 'https://api.fabdb.net'
cards_uri = '/cards'
folder_name = 'card_images/'
#response = requests.get(api_url)
response = requests.get(api_url + cards_uri + '/UPR000')
#print(response.json())
json_dict = response.json()
#cardData = json.loads(response.json())
cardData = Card(json_dict["identifier"], json_dict["rarity"], json_dict["keywords"], json_dict["stats"], json_dict["image"])
print(vars(cardData))

cardList = []
# UPR000 - UPR223
for i in range(224):
    cardid = f'/UPR{i:03d}'
    response = requests.get(api_url + cards_uri + cardid)    
    json_dict = response.json()
    card = Card(json_dict["identifier"], json_dict["rarity"], json_dict["keywords"], json_dict["stats"], json_dict["image"])
    cardList.append(card)

    # Download the card image
    r = requests.get(card.image_url, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True

        with open(folder_name + json_dict["identifier"] + '.png', 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    print('added ' + cardid)
    time.sleep(1)

f = open("cards.json", "w")
f.write(jsonpickle.encode(cardList, cls=CardEncoder))
f.close()