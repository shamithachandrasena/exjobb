# Script to edits the json file to create a pick sequence

import json
import random
import time

class Place:
    def __init__(self, item_id, x, y):
        self.item_id = item_id
        self.x = x
        self.y = y

A01 = Place('A01', 120, 150)
A02 = Place('A02', 240, 125)
A03 = Place('A03', 120, 150)
A04 = Place('A04', 240, 125)
A05 = Place('A05', 120, 150)
A06 = Place('A06', 240, 125)
A07 = Place('A07', 120, 150)
A08 = Place('A08', 240, 125)
A09 = Place('A09', 120, 150)
A10 = Place('A10', 240, 125)
A11 = Place('A11', 120, 150)
A12 = Place('A12', 240, 125)
A13 = Place('A13', 120, 150)
A14 = Place('A14', 240, 125)
A15 = Place('A15', 120, 150)
A16 = Place('A16', 240, 125)
A17 = Place('A17', 120, 150)
A18 = Place('A18', 240, 125)

places = [A01, A02, A03, A04, A05, A06, A07, A08, A09, A10, A11, A12, A13, A14, A15, A16, A17, A18]

def get_random_place():
    return random.choice(places)


def update_data():
    global data
    with open('example.json') as json_file:
        data = json.load(json_file)
        json_file.close()

while(True):
    update_data()
    if data['picked'] == 1:
        print('Updated')
        time.sleep(3)
        place = get_random_place()
        data['item_id'] = place.item_id
        data['x-axis'] = place.x
        data['y-axis'] = place.y
        data['picked'] = 0
        with open('example.json', 'w') as outfile:
            json.dump(data, outfile)
            outfile.close()
    else:
        time.sleep(0.1)

