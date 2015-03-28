#!/usr/bin/env python
import os
import re
import sys

SUFFIX_PAT = re.compile(r'(?P<FILE>[a-zA-z0-9]+)_\d+\b')
SUFFIXED_LIST = []


def is_suffixed_file(dir_path, file_name):
    base_name, ext_name = os.path.splitext(file_name)
    match_obj = SUFFIX_PAT.match(base_name)
    if not match_obj:
        return False

    no_suffixed_file = os.path.join(dir_path, match_obj.group('FILE') + ext_name)
    if not os.path.exists(no_suffixed_file):
        return False

    return True


def collect_suffixed_file(dir_path, file_name):
    if not is_suffixed_file(dir_path, file_name):
        return

    suffix_file = os.path.join(dir_path, file_name)
    SUFFIXED_LIST.append(suffix_file)


def remove_files():
    if not SUFFIXED_LIST:
        print 'No suffixes file.'
        return

    SUFFIXED_LIST.sort()
    for name in SUFFIXED_LIST:
        print name

    input_str = raw_input('Do you want to remove this files: [Y/N]')
    if input_str.upper() != 'Y':
        return

    for name in SUFFIXED_LIST:
        try:
            os.remove(name)
            print '%s removed.' % name
        except OSError, e:
                print e


def main():
    if len(sys.argv) < 2:
        print 'Please a directory.'
        return

    if not os.path.isdir(sys.argv[1]):
        print 'Please input valid path - %s' % sys.argv[1]
        return

    for dir_path, dir_list, file_list in os.walk(sys.argv[1]):
        for file_name in file_list:
            collect_suffixed_file(dir_path, file_name)

    remove_files()

if __name__ == '__main__':
    main()
