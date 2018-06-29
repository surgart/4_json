import sys
import json

def load_data(filepath):
    with open(filepath, encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    return json_data


def pretty_print_json(json_data):
    print(json.dumps(json_data, indent=4, sort_keys=True))


if __name__ == '__main__':
    filepath = sys.argv[1]
    json_data = load_data(filepath)
    # pretty_print_json(json_data)
    with open('pprint_output.json', 'w+', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)
