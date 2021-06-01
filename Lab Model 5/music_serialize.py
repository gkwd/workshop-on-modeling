import os
import pickle
import json

FILENAME_PICKLE = 'group.pickle'
FILENAME_JSON = 'group.json'

my_favourite_group = {
    'name':  'AC/DC',
    'tracks': ['Back in Black', 'Highway to hell'],
    'albums': [
        {
            'name': 'Back in Black',
            'year': '1980'
        },
        {
            'name': 'Power up',
            'year': '2020'
        }
    ]
}

def toJson(data):
    return json.dumps(data)

def writeJson(data, filename, encoding='utf-8'):
    with open(filename, 'w', encoding=encoding) as out_f:
        json.dump(data, out_f)

def toPickle(data):
    return pickle.dumps(data)

def writePickle(data, filename):
    with open(filename, 'wb') as out_f:
        pickle.dump(data, out_f)

group_data_pickle = toPickle(my_favourite_group)
print(f'\nPickle: \t{group_data_pickle}')

group_data_json = toJson(my_favourite_group)
print(f'\nJSON: \t{group_data_json}')

writeJson(group_data_json, FILENAME_JSON)
if os.path.exists(FILENAME_JSON):
    print(f'Данные записаны в файл (json) {FILENAME_JSON}')

writePickle(group_data_pickle, FILENAME_PICKLE)
if os.path.exists(FILENAME_PICKLE):
    print(f'Данные записаны в файл (pickle) {FILENAME_PICKLE}')