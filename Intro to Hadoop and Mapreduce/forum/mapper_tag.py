#! /usr/bin/python

import sys
import csv
import re
import collections

N = 10

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    tags=collections.defaultdict(int)

    for line in reader:
        if(len(line)) == 19:
            id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
            
            if node_type!='question':
                continue
            
            tag_list=tagnames.split(' ')
            for tag in tag_list:
                tags[tag]+=1

    for tag,count in tags.items():
        print '{0}\t{1}'.format(tag, count)

if __name__ == "__main__":
    mapper()
