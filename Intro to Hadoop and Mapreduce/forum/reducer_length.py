#! /usr/bin/python

import sys
import re

def reducer():
    total_ans_length=0
    question_length=0
    count=0
    prev_id=None
    for line in sys.stdin:
        data=line.strip().split('\t')
        if len(data)!=3:
            continue
        
        curr_id,type_post,curr_len=data      
       
        if prev_id and curr_id!=prev_id:
            print prev_id,'\t',question_length,'\t',total_ans_length*1.0/count if count>0 else 0
            question_length=0
            total_ans_length=0
            count=0
        if type_post=='Q':
            question_length=int(curr_len)
        else:
            count+=1
            total_ans_length+=int(curr_len)
          

        prev_id=curr_id
    
    if prev_id:
        print prev_id,'\t',question_length,'\t',total_ans_length*1.0/count if count>0 else 0       

if __name__ == "__main__":
    reducer()
