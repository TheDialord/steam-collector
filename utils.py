import fileinput
import os
import json

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def open_file_line(path):
    line = None
    with open(os.path.join(APP_ROOT, path), "r") as f:
        data = json.load(f)
        line = data[0]

        data = data[1:]
        with open(os.path.join(APP_ROOT, path), 'w+') as _f:
            json.dump(data, _f)
    return line


def open_file_lines(path):
    with open(os.path.join(APP_ROOT, path), "r") as f:
        data = json.load(f)
        return data


def add_file_line(path, line):
    with open('data.json', 'r') as f:
        data = json.load(f)
        data.insert(0, line)

    with open('data.json', 'w') as f:
        json.dump(data, f)
        return True

