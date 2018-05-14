#! /usr/bin/python

import sys

count=0
old_key=None
max_key=None
max_count=0


for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    this_key, this_status = data
 

    if old_key and this_key!=old_key:
        if not max_key or count>max_count:
            max_key=this_key
            max_count=count
        count=0
    
    old_key=this_key
    count+=1

if old_key and this_key!=old_key:
    if not max_key or count>max_count:
        max_key=this_key
        max_count=count
    

if max_key !=None:
    print "The most popular site is",max_key,"with",max_count,"times click"


    

