#!/usr/bin/env python2
#-*- coding: utf-8 -*-

import sys
import youtube_dl


def main():
    if len(sys.argv) < 2:
        print("Usage: youtube_dl_op_sample.py URL")
        return

    opts = { 
            'forceurl': True,
            'quiet': True,
            'simulate': True,
            }

    url = sys.argv[1]

    try:
        with youtube_dl.YoutubeDL(opts) as ydl:
            extract_info = ydl.extract_info(url)
            resource_uri = extract_info.get('url')

            if not resource_uri:
                format_id = extract_info.get('format_id')
                for fmt in extract_info.get('formats'):
                    if format_id != fmt.get('format_id'):
                        continue
                    resource_uri = fmt.get('url')
    except Exception as e:
        print(e)
        resource_uri = None

    if resource_uri:
        print("resource_uri: %s" % resource_uri)
    else:
        print("Nothing at all.")

if __name__ == '__main__':
    main()
