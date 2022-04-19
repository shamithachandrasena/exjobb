import json

with open('example.json') as json_file:
    data = json.load(json_file)

print(data['mode'])