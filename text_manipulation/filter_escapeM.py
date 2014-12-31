#!/usr/bin/env python2.7
import sys

def main():
    if len(sys.argv) < 2:
        print "Input a file"
        return False

    try:
        fp = open(sys.argv[1], 'r+')
        try:
            file_str = fp.read()
            fp.truncate()
        finally:
            fp.close()
    except IOError, e:
        print e
        return False

    #file_str.replace(r'\r', '')
    file_str = ''.join(file_str.split(r'\r'))

    try:
        fp = open(sys.argv[1], 'w')
        try:
            print file_str
            fp.write(file_str)
        finally:
            fp.close()
    except IOError, e:
        print e
        return False


    return True

if __name__ == '__main__':
    main()
