#!/usr/bin/env python2
#coding=utf-8
import os
import sys
import lxml.etree
import urllib2

def download(url, file_name, work_path='.'):
    assert isinstance(url, str)
    try:
        response = urllib2.urlopen('%s' % url)
    except urllib2.HTTPError, e:
        sys.stderr.write('%s\n' %e)
        sys.stderr.write("Could not retrieve file: %s\n" % url)
        return

    save_path = os.path.join(work_path, os.path.basename(file_name + '.torrent'))
    fp = open(save_path, 'w')
    fp.write(response.read())
    fp.close()
    print 'Download %s done.' % save_path


def process_sub_page(target_url, base_url, title):
    if not target_url:
        print '{} not found.'.format(sys.argv[1])
        return

    response = urllib2.urlopen(target_url)
    content = response.read()
    page = lxml.etree.HTML(content.decode('utf-8'))
    for href in page.xpath(u"//a"):
        if not href.text:
            continue

        if u'点击此处下载种子' in href.text:
            torrent = base_url.format(href.attrib.get('href'))
            print torrent
            download(torrent, title)

        if u'使用磁力链下载' in href.text:
            print href.text.strip(), ':'
            print href.attrib.get('href')
    print '\n'



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
            process_sub_page(target_url, base_url, href.text.strip())


if __name__ == '__main__':
    sys.argv.extend(['20150126'])
    main()