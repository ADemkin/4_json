'''
Prints out a json file in a pretty prent format.

Usage: pprint_json.py [path]

Anton Demkin, 2017
antondemkin@yandex.ru
'''

import json
import sys
import os


def pretty_print_json(json_data):
    print(json.dumps(json_data, sort_keys=True, indent=4, ensure_ascii=False))


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if not os.path.exists(path):
            print("%s is not correct path." % str(path))
        else:
            with open(path) as file:
                json_data = json.load(file)
                pretty_print_json(json_data)


if __name__ == '__main__':
    main()
