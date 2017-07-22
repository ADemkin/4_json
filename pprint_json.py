import json
import sys
import os

def load_json(filepath):
    with open(filepath) as file:
        json_data = json.load(file)
        return json_data

def pretty_print_json(json_data):
    print(json.dumps(json_data, sort_keys=True, indent=4, ensure_ascii=False))


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.exists(path):
            try:
                json_data = load_json(path)
                pretty_print_json(json_data)
            except Exception as error:
                print('Error: %s' % error)
        else:
            print('%s not found.' % path)
    else:
        print('Usage: pprint_json.py [file]')


if __name__ == '__main__':
    main()
