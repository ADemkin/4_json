import json
import sys


def load_json(filepath):
    with open(filepath) as file:
        json_data = json.load(file)
        return json_data


def pretty_print_json(json_data):
    print(json.dumps(json_data, sort_keys=True, indent=4, ensure_ascii=False))


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        try:
            json_data = load_json(path)
            pretty_print_json(json_data)
        except Exception as error:
            print('Error: %s' % error)
    else:
        print('Usage: pprint_json.py [file]')


if __name__ == '__main__':
    main()
