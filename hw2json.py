import json
from pprint import pprint

orders = {}

def write_order_to_json():
    '''
    orders['item'] = input('Input item name: ')
    orders['quantity'] = int(input('Input quantity: '))
    orders['price'] = input('Input price: ')
    orders['buyer'] = input('Input buyer: ')
    orders['date'] = input('Input date: ')
    '''
    orders['item'] = 'AK-74'
    orders['quantity'] = 1000
    orders['price'] = 450
    orders['buyer'] = 'unknown'
    orders['date'] = '12/11/1987'

write_order_to_json()

with open('orders.json', 'w') as file:
    json.dump(orders, file, indent = 4)

with open('orders.json') as file:
    pprint(json.load(file))
