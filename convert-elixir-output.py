#Python

import os
import sys

script_dir = os.path.dirname(__file__)

#abs_file_path = os.path.join(script_dir, rel_path)

def main():

    rel_path = raw_input('Specify source file path: ')
    target_path = raw_input('Specify target file path: ')

    with open(rel_path) as f:
        with open(target_path, "w+") as t:
            str = f.read()
            str = str.replace('], ', '\n')
            str = str.replace('[', '')
            str = str.replace('"', '')
            str = str.replace(',', '\t')

            t.write(str)

            t.close()
            if t.closed:
                print 'Target file closed'
            else: print 'ERROR'

        f.close()
        if f.closed:
            print 'Source file closed'
        else: print 'ERROR'

    print ('DONE')



if __name__ == '__main__':
    main()