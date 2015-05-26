import os
import json

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def open_file_line(path):
    line = None
    try:
        with open(os.path.join(APP_ROOT, path), "r") as f:
            data = json.load(f)
            line = data['listings'][0]

            data['listings'] = data['listings'][1:]
            with open(os.path.join(APP_ROOT, path), 'w+') as _f:
                json.dump(data, _f)

    except:
        pass

    return line


def add_file_line(path, line):
    try:
        with open(os.path.join(APP_ROOT, path), 'r') as f:
            data = json.load(f)
            data['listings'].insert(0, line)

        with open(os.path.join(APP_ROOT, path), 'w') as f:
            json.dump(data, f)
            return True
    except:
        return None


def open_items(path):
    try:
        with open(os.path.join(APP_ROOT, path), "r") as f:
            data = json.load(f)
            return data['items']
    except:
        return None