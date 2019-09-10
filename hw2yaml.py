import yaml
from pprint import pprint

data = {'item': 'AK-74',
        'quantity': 1000,
        'price': 450,
        'dates': [7, 14, 21, 28]}


with open('file.yml', 'w') as file:
    yaml.safe_dump(data, file)


with open('file.yml') as file:
    pprint(yaml.safe_load(file))
