import json

def load_json(name):
    with open(f'data/{name}.json') as json_file:
        if json_file:
            return json.load(json_file)
        else:
            return []

def save_json(name, data):
    with open(f'data/{name}.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)