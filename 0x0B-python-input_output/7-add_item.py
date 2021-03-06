#!/usr/bin/python3
""" script that adds all arguments to a Python list,
and then save them to a file"""


if __name__ == "__main__":
    import json
    import sys
    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file').load_from_json_file

    try:
        file = load_from_json("add_item.json")
    except:
        file = []

    file += sys.argv[1:]
    save_to_json(file, "add_item.json")
