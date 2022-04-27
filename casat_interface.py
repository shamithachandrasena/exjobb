import json

data = None

def update_data():
    global data
    with open('example.json') as json_file:
        data = json.load(json_file)

# Returns mode, which is either Pick, Place or Setup
def get_mode():
    return data['mode']

# Returns x coordinate
def get_x_axis():
    return data['x-axis']

# Returns y coordinate
def get_y_axis():
    return data['y-axis']

# Returns height
def get_height():
    return data['height']

# Returns item
def get_item():
    return data['item']
