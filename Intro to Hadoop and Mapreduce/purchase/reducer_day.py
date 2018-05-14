#! /usr/bin/python

import sys

sales_total = 0
count=0
old_key = None


for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    this_key, this_sale = data

    if old_key and old_key != this_key:
        print old_key,"Total is",sales_total,"and the average is",sales_total*1.0/count
        sales_total = 0
        count=0

    old_key = this_key
    sales_total += float(this_sale)
    count+=1
    

if old_key != None:
    print old_key,"Total is",sales_total,"and the average is",sales_total*1.0/count

