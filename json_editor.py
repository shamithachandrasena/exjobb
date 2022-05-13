# Script to edits the json file to create a pick sequence

import json
import random
import time

class Place:
    def __init__(self, item_id, x, y):
        self.item_id = item_id
        self.x = x
        self.y = y

A04 = Place('A04', 5, 142)
A05 = Place('A05', 50, 122)
A06 = Place('A06', 79, 93)
A07 = Place('A07', 20, 175)
A08 = Place('A08', 115, 155)
A09 = Place('A09', 315, 150)
A10 = Place('A10', 400, 170)
A11 = Place('A11', 120, 150)
A12 = Place('A12', 275, 112)
A13 = Place('A13', 412, 135)
A14 = Place('A14', 360, 117)
A15 = Place('A15', 343, 84)

places = [A04, A05, A06, A07, A08, A09, A10, A11, A12, A13, A14, A15]

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

