#! /usr/bin/env python2
'''
Created on Oct 30, 2014

@author: daineseh
'''
import os, sys

def split_by_semicolon(data):
    assert isinstance(data, str)

    cur_pos = 0
    start_pos = 0
    splited_list = []

    while(cur_pos != -1):
        cur_pos = data.find(';', start_pos)
        if cur_pos == -1:
            splited_list.append(data[start_pos:len(data)])
            break
        next_pos = cur_pos + 1
        splited_list.append(data[start_pos:next_pos])
        start_pos = next_pos

    striped_list = map(lambda x: x.strip(), splited_list)
    return filter(lambda x: x, striped_list)


def main():
    if not len(sys.argv) > 1:
        return

    if not os.path.exists(sys.argv[1]):
        print "[ERROR] Path not exists. (%s)" % sys.argv[1]
        return

    fp = open(sys.argv[1])
    print split_by_semicolon(fp.read())


if __name__ == '__main__':
    main()