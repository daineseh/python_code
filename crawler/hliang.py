#!/usr/bin/env python2
#coding=utf-8
import sys
import lxml.etree
import urllib2

def main():
    if len(sys.argv) == 1:
        print 'Usage: hliang.py SEARCH_KEY_WORD'
        return

    base_url = 'http://bt.hliang.com/{}'
    url = base_url.format('index.php')
    target_url = ''

    response = urllib2.urlopen(url)
    content = response.read()
    page = lxml.etree.HTML(content.decode('utf-8'))
    hrefs = page.xpath(u"//a")
    for href in hrefs:
        if not href.text:
            continue

        if sys.argv[1] in href.text:
            target_url = base_url.format(href.attrib.get('href'))
            print href.text.strip()

    if not target_url:
        print '{} not found.'.format(sys.argv[1])
        return

    response = urllib2.urlopen(target_url)
    content = response.read()
    page = lxml.etree.HTML(content.decode('utf-8'))
    for href in page.xpath(u"//a"):
        if not href.text:
            continue

        if u'使用磁力链下载' in href.text:
            print href.text.strip(), ':'
            print href.attrib.get('href')

if __name__ == '__main__':
    main()