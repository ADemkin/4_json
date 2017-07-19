import json
import sys


def pretty_print_json(json_data):
    print(json.dumps(json_data, sort_keys=True, indent=4, ensure_ascii=False))


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        with open(path) as file:
            json_data = json.load(file)
            pretty_print_json(json_data)


if __name__ == '__main__':
    main()
