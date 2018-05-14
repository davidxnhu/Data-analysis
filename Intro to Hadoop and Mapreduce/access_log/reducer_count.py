#! /usr/bin/python

import sys

count=0
old_key=None


for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    this_key, this_status = data

    if old_key and this_key!=old_key:
        print "{0}\t{1}".format(old_key,count)
        count=0
    
    old_key=this_key
    count+=1
    

if old_key !=None:
    print "{0}\t{1}".format(old_key,count)

    

