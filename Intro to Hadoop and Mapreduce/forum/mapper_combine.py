#! /usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line) == 5:
        # forum_users.tsv
        if str(line[0]).isdigit():  # don't print header
            writer.writerow([int(line[0])] + ['A'] + line[1:])

    if len(line) == 19:
        # forum_node.tsv
        if str(line[0]).isdigit():  # don't print header
            writer.writerow([int(line[3])] + ['B'] + line[0:3] + line[5:10])
