import json

with open('input.json', 'r') as input:
    object = json.load(input)
    print('Hello, ' + object['name'])
