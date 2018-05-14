#! /usr/bin/python

import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    try:
        if len(line)==19:
            author_id=line[3]
            date=line[8][:-3]
            index=date.find('.')
            if index!=-1:
                date=date[:index]
            date=datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            print "{0}\t{1}".format(author_id,date.hour)
    except:
        continue
