#! /usr/bin/python

import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if(len(line)) == 19:
            id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
            
            # Output "Q" for questions, and "Z" for answers in the second column, to have questions appear before answers (just for posterity)
            if(node_type == 'question'):
                print "{0}\t{1}\t{2}".format(id, "Q", len(body))
            elif(node_type == 'answer'):
                print "{0}\t{1}\t{2}".format(abs_parent_id, "A", len(body))

if __name__ == "__main__":
    mapper()
