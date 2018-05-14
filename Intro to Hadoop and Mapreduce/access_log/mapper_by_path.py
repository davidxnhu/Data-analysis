#! /usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, identity, username, datetime, tz, method, page, http_version, status, content_size = data

        if page.find('http://www.the-associates.co.uk')!=-1:
            page=page[len('http://www.the-associates.co.uk'):]
        print "{0}\t{1}".format(page, 1)
