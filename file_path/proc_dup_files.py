#!/usr/bin/env python2
import os
import sys


def main():
    if len(sys.argv) < 2:
        print 'Input a directory.'
        return False

    if not os.path.isdir(sys.argv[1]):
        print 'Invalid directory - %s' % sys.argv[1]

    name_list = []
    duplicate_list = []
    for dir_path, dir_list, file_list in os.walk(sys.argv[1]):
        for file_name in file_list:
            lowercase = file_name.lower()
            if lowercase not in name_list:
                name_list.append(lowercase)
                continue
            path = os.path.join(dir_path, file_name)
            duplicate_list.append(path)

    for dup_path in duplicate_list:
        print dup_path

    if duplicate_list:
        print '-' * 12
        print 'Total %s files is duplicated.' % len(duplicate_list)
        input_str = raw_input('Do you want to remove this files: [Y/N]')
        if input_str.upper() == 'Y':
            for idx, dup in enumerate(duplicate_list, start=1):
                try:
                    os.remove(dup)
                    print '[%s]%s removed.' % (idx, dup)
                except OSError, e:
                        print e
    else:
        print 'No duplicate file.'

    return True


if __name__ == '__main__':
    main()

