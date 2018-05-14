#! /usr/bin/python

import sys
import csv
import re
import string



reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)


for line in reader:
    try:
        if len(line) == 19:
	    node_id = int(line[0].strip())
	    body = line[4]
            body_words = re.findall(r"[a-zA-Z]+", body)  #  '[a-zA-Z]+' # means "a word character (a-z A-Z etc.) repeated one or more times
            for word in body_words:
                print "{0}\t{1}".format(word.lower(), node_id)
    except:
        continue
    

