#!/usr/bin/env python3

import os
import sys
import zipfile


def main():
    if len(sys.argv) < 2:
        print("zip-folder: Specified a directory, and Zip all sub directorys in this directory.")
        print("Usage: $zip-folder.py DIR")
        return False

    if not os.path.isdir(sys.argv[1]):
        print('Invalid directory - %s' % sys.argv[1])

    for dir_path, dir_list, file_list in os.walk(sys.argv[1]):
        for dir_name in dir_list:
            zf = zipfile.ZipFile(dir_name + '.zip', mode = 'w', compression = zipfile.ZIP_DEFLATED)
            path = os.path.join(dir_path, dir_name)
            for root, _, files in os.walk(path):
                for name in files:
                    zf.write(os.path.join(root, name))
            print("Compress [%s] done." % path)
            zf.close()



if __name__ == '__main__':
    main()
