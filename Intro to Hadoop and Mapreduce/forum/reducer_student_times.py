#! /usr/bin/python

import sys

prev_author=None
time_record={}

for line in sys.stdin:
    data=line.strip().split('\t')
    
    if len(data)!=2:
        continue
    
    author_id,hour=data
    
    if author_id != prev_author:
        if time_record.values():
            max_count=max(time_record.values())
            max_hour=[hour for hour in time_record if time_record[hour]==max_count]
        
            for hour in max_hour:
                print prev_author,hour
        
        time_record={}
    
    if hour in time_record:
        time_record[hour]+=1
    else:
        time_record[hour]=1
    
    prev_author=author_id

if prev_author:
    max_count=max(time_record.values())
    max_hour=[hour for hour in time_record if time_record[hour]==max_count]
        
    for hour in max_hour:
        print prev_author,hour
