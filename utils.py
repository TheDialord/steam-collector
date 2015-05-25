import fileinput
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def open_file_line(path):
    with open(os.path.join(APP_ROOT, path), "r") as ins:
        for line in ins:
            return line
        with open(os.path.join(APP_ROOT, path), 'w') as fout:
            fout.writelines(ins[1:])

    return None


def open_file_lines(path):
    with open(path) as f:
        lines = f.readlines()
    return lines


def add_file_line(path, line):
    for linenum, line in enumerate(fileinput.FileInput(os.path.join(APP_ROOT, path), inplace=1)):
        if linenum == 0:
            print line
            print line.rstrip()
        else:
            print line.rstrip()