#!/usr/bin/env python2
import os
import sys
import tarfile

def main():
    base_path = '../../'
    absolute_path = os.path.abspath(base_path)

    compress_files = []
    compress_files.append(os.path.join(absolute_path, 'path1'))
    compress_files.append(os.path.join(absolute_path, 'path2'))
    compress_files.append(os.path.join(absolute_path, 'path3'))
    compress_files.append(os.path.join(absolute_path, 'path4'))
    compress_files.append(os.path.join(absolute_path, 'path5'))

    if len(sys.argv) > 1:
        arc_name = sys.argv[1]
    else:
        arc_name = 'fw.tar.bz2'
    fp = tarfile.open(arc_name, mode='w:bz2')
    for name in compress_files:
        print 'Archive: ', name
        fp.add(name, arcname=os.path.basename(name))
    fp.close()

if __name__ == '__main__':
    '''
    $> ./archive_files.py
    or
    $> ./archive_files.py ARCHIVE_FILES
    '''
    main()
