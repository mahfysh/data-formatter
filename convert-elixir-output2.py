# Python

import os
import sys
from tkinter import Tk, filedialog
import re


def extract_string():

    for _ in f:
        content = f.readline()
        content = re.search('KingsPay(.+?)\\\\",', content)

        if content:
            found = content.group(0)
            found = found.replace('\\",', "\n")
            t.write(found)


def change_string(f, t):

    if f:
        print('Files found')
    else:
        print('Error: File not found')

    for remove in ['{', '[', ']']:
        content = f.read()
        content = content.replace(remove, '')
        content = content.replace('},', '\n')
        t.write(content)


def delete_line(f, t):

    for _ in f:

        content = f.readline()
        test = re.search('failed', content)
        if test:
            t.write(content)


def open_files():
    root = Tk()
    root.withdraw()
    rel_path = filedialog.askopenfilename()
    root.destroy()

    while True:
        target_path = os.path.dirname(rel_path)
        filename = input('Specify filename: ')
        target_path = target_path + '/' + filename + '.txt'
        if target_path == rel_path:
            print('Target filename cannot be the same as source filename.')
        else:
            break

    with open(rel_path, "r") as f:

        with open(target_path, "w+") as t:

            delete_line(f, t)

    print('File created at: ' + target_path)


def main():

    print(sys.version)
    open_files()
    print('DONE')


if __name__ == '__main__':
    main()
