#!/usr/bin/env python2

import re
import subprocess as sub
import sys

LENGTH_PAT = re.compile('[\s]length[\s](?P<NUM>\d+)')
WHITE_SPACE_PAT = re.compile("^([\s]+)")

def traffic_counter(port_num):
    length = 0

    try:
        p = sub.Popen(('sudo', 'tcpdump', '-nnnx', 'port', port_num), stdout=sub.PIPE)
    except OSError, e:
        print e
        return
    except ValueError, e:
        print e
        return

    for row in iter(p.stdout.readline, b''):
        row_str = row.rstrip()

        # Prefilter
        if WHITE_SPACE_PAT.match(row_str):
            continue
        elif ", length 0" in row_str:
            continue

        match_obj = LENGTH_PAT.search(row_str)
        if not match_obj:
            continue

        length += int(match_obj.group('NUM'))
        print length


def main():
    if len(sys.argv) < 2:
        print "Please input port number."
        sys.exit(0)
    traffic_counter(sys.argv[1])

if __name__ == '__main__':
    main()
