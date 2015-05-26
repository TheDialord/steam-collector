import os
import ujson

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def open_file_line(path):
    line = None
    with open(os.path.join(APP_ROOT, path), "r") as f:
        data = ujson.load(f)
        line = data[0]

        data = data[1:]
        with open(os.path.join(APP_ROOT, path), 'w+') as _f:
            ujson.dump(data, _f)
    return line


def open_file_lines(path):
    with open(os.path.join(APP_ROOT, path), "r") as f:
        data = ujson.load(f)
        return data


def add_file_line(path, line):
    with open('data.json', 'r') as f:
        data = ujson.load(f)
        data.insert(0, line)

    with open('data.json', 'w') as f:
        ujson.dump(data, f)
        return True

