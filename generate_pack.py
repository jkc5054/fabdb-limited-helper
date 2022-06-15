from ast import keyword
import json
import random
from collections import namedtuple
from json import JSONEncoder

from pyparsing import And
from scipy import rand
from card import Card

def customCardDecoder(cardDict):
    return namedtuple('X', cardDict.keys())(*cardDict.values())

#f = open("cards.json", 'r')
#cards_json = f.read()

#cardJSON = json.loads(cards_json)
#print(cardJSON)

with open('cards.json', 'r') as data_file:
    json_data = data_file.read()

data = json.loads(json_data, object_hook=customCardDecoder)
#print(data[0].identifier)

#pack structure
# first 3 cards => generic common, draconic common, ice common
# 4th card => common equipment
# 5th card => rare
# 6th card => rare+
# 7th card => foil
# 8th - 14th cards => ninja, wizard, or illu commons

talent_slot = []
equipment_slot = []
rare_slot = []
majestic_list = []
foil_slot = []
class_slot = []

for i in data:
    # populate the talent_slot
    if (i.rarity == 'C' and  
    ('generic' in i.keywords or 'draconic' in i.keywords or 'ice' in i.keywords) and 
    ('wizard' not in i.keywords and 'illusionist' not in i.keywords and 'ninja' not in i.keywords) and
    'equipment' not in i.keywords
    ):
        talent_slot.append(i)
    
    # populate the equipment
    if(i.rarity == 'C' and 'equipment' in i.keywords):
        equipment_slot.append(i)

    # populate the rare slot
    if(i.rarity == 'R'):
        rare_slot.append(i)

    # populate the majestics
    if(i.rarity == 'M'):
        majestic_list.append(i)
    
    # populate the foil slot
    if(i.rarity == 'C'):
        foil_slot.append(i)
    
    # populate the class slot
    if(i.rarity == 'C' and 'equipment' not in i.keywords and ('wizard' in i.keywords or 'illusionist' in i.keywords or 'ninja' in i.keywords)):
        class_slot.append(i)

pack = []
pack.append(random.choice(talent_slot))
pack.append(random.choice(talent_slot))
pack.append(random.choice(talent_slot))
pack.append(random.choice(equipment_slot))
pack.append(random.choice(rare_slot))
# for rare+, 1 in 4 chance to hit a majestic
if(random.randint(1, 4) == 4):
    pack.append(random.choice(majestic_list))
else:
    pack.append(random.choice(rare_slot))
pack.append(random.choice(foil_slot))
pack.append(random.choice(class_slot))
pack.append(random.choice(class_slot))
pack.append(random.choice(class_slot))
pack.append(random.choice(class_slot))
pack.append(random.choice(class_slot))
pack.append(random.choice(class_slot))
pack.append(random.choice(class_slot))

for i in pack:
    print(i.identifier)
