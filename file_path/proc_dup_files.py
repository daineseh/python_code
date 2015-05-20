#!/usr/bin/env python2
import os
import sys


def convert_bytes(bytes):
    bytes = float(bytes)
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.2fT' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2fG' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2fM' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2fK' % kilobytes
    else:
        size = '%sb' % bytes
    return size

def main():
    if len(sys.argv) < 2:
        print 'Input a directory.'
        return False

    if not os.path.isdir(sys.argv[1]):
        print 'Invalid directory - %s' % sys.argv[1]

    name_list = []
    duplicate_list = []
    size_count = 0
    for dir_path, dir_list, file_list in os.walk(sys.argv[1]):
        for file_name in file_list:
            lowercase = file_name.lower()
            if lowercase not in name_list:
                name_list.append(lowercase)
                continue
            path = os.path.join(dir_path, file_name)
            duplicate_list.append(path)

            statinfo = os.stat(path)
            size_count += statinfo.st_size

    for dup_path in duplicate_list:
        statinfo = os.stat(dup_path)
        print '%s - %s' % (dup_path, convert_bytes(statinfo.st_size))

    if duplicate_list:
        print '-' * 12
        print 'Total %s files is duplicated. (%s)' % (len(duplicate_list), convert_bytes(size_count))
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

