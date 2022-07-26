import requests
import shutil
import json
import time

from main.model.card import Card
from main.model.card import CardEncoder



api_url = 'https://api.fabdb.net'
cards_uri = '/cards'
response = requests.get(api_url + cards_uri + '/UPR000')
json_dict = response.json()
image_url = json_dict["image"]
filename = 'UPR000.png'

r = requests.get(image_url, stream = True)

if r.status_code == 200:
    r.raw.decode_content = True

    with open(filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

    print('image successfully downloaded: ', filename)
else:
    print('image couldn\'t be retrieved')