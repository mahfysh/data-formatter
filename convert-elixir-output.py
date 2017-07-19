# Python

import os
import sys
from tkinter import Tk, filedialog


def main():
    print(sys.version)
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

    with open(rel_path) as f:

        with open(target_path, "w+") as t:

            content = f.read()
            content = content.replace('], ', '\n')
            content = content.replace('[', '')
            content = content.replace('"', '')
            content = content.replace(',', '\t')
            t.write(content)
            print('File created at: ' + target_path)
            t.close()
            if not t.closed:
                print('Target file not closed')

        f.close()
        if not f.closed:
            print('Source file not closed')

    print('DONE')


if __name__ == '__main__':
    main()
