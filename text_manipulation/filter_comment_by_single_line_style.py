#! /usr/bin/env python2
'''
Created on Oct 29, 2014

@author: daineseh
'''


def comment_filter(comment_char, file_path):
    assert isinstance(file_path, str)

    filtered_list = []

    for line in open(file_path):
        li = line.strip()
        if li.startswith(comment_char):
            continue
        filtered_list.append(line)

    return ''.join(filtered_list)


if __name__ in '__main__':
    import sys
    print comment_filter('#', sys.argv[1])
