import json

data = {}

def update_data():
    global data
    with open('example.json') as json_file:
        data = json.load(json_file)
        json_file.close()

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
    return data['item_id']

# Write to file
def write_to_file(key, value):
    data[key] = value 
    with open('example.json', 'w') as outfile:
        json.dump(data, outfile)
        outfile.close()

