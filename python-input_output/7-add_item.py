#!/usr/bin/python3
import sys
import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """Creates an Object from a JSON file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

filename = "add_item.json"
my_list = load_from_json_file(filename)

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, filename)