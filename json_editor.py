# Script to edits the json file to create a pick sequence

import json
import random
import time

class Place:
    def __init__(self, item_id, x, y):
        self.item_id = item_id
        self.x = x
        self.y = y

A04 = Place('A04', 22, 154)  #
A05 = Place('A05', 65, 130)  #
A06 = Place('A06', 99, 93)   #
A07 = Place('A07', 60, 182)  #
A08 = Place('A08', 145, 163) #
A09 = Place('A09', 171, 122) #
A10 = Place('A10', 430, 190) #
A11 = Place('A11', 338, 167) #
A12 = Place('A12', 301, 124) #
A13 = Place('A13', 444, 158) #
A14 = Place('A14', 400, 135) #
A15 = Place('A15', 360, 102) #

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

