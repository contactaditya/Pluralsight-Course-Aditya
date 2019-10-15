import json

with open('input.json', 'r') as input:
    object = json.load(input)
    with open('output.txt', 'w') as output:
        output.write(object['name'] + "'s Hobbies:\n")
        for hobby in object['hobbies']:
            output.write(hobby + "\n")
