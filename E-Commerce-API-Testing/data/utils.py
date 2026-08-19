import os
import json


def load_user_data(key):
    '''
    locates the centralized JSON file and pulls specific user credencial dictionaries.
    '''
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'users.json')
    file_path = os.path.abspath(file_path)
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)

    return data.get(key)
