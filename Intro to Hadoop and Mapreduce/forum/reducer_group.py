#! /usr/bin/python

import sys

def reducer():
    student_list=[]
    old_id = None
    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) !=2:
            continue
 
        this_id,this_author=data
        if old_id and this_id != old_id:
            print old_id, '\t', student_list
            student_list=[]
           
        student_list.append(this_author)
        old_id=this_id
    
    if old_id:
        print old_id, '\t', student_list

if __name__ == "__main__":
    reducer()
