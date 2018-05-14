#! /usr/bin/python

import sys

sales_total = 0
count=0


for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    this_key, this_sale = data

    count+=1
    sales_total+=float(this_sale)
    

if count != 0:
    print "Total count\t",count
    print "Total sales\t",sales_total
    

