#! /usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, identity, username, datetime, tz, method, page, http_version, status, content_size = data
        print "{0}\t{1}".format(ip, 1)
