#! /usr/bin/python

import sys
import csv


old_uid = None
curr_user = None
entries = list()

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    if len(line) == 10:
        uid, _, pid, title, tag_names, node_type, parent_id, abs_parent_id, added_at, score = line
    elif len(line) == 6:
        uid, _, reputation, gold, silver, bronze = line
        curr_user = {'uid': uid, 'reputation': reputation, 'gold': gold, 'silver': silver, 'bronze': bronze}
    else:
        continue

    if old_uid is not None and uid != old_uid:
        # print pending entries
        for entry in entries:
            if curr_user is not None:
                print('\t'.join([entry['pid'], entry['title'], entry['tag_names'], curr_user['uid'], entry['node_type'],entry['parent_id'], entry['abs_parent_id'], entry['added_at'], entry['score'],curr_user['reputation'], curr_user['gold'], curr_user['silver'], curr_user['bronze']]))
        curr_user = None
        entries = list()

    if curr_user is not None and len(line) == 10:
        # if we have the user entry and current line is a post entry
        print('\t'.join([pid, title, tag_names, curr_user['uid'], node_type, parent_id, abs_parent_id, added_at, score,curr_user['reputation'], curr_user['gold'], curr_user['silver'], curr_user['bronze']]))
    elif curr_user is None and len(line) == 10:
        # we don't have the user entry and current line is a post entry
        entries.append({'uid': uid, 'pid': pid, 'title': title, 'tag_names': tag_names, 'node_type': node_type,'parent_id': parent_id, 'abs_parent_id': abs_parent_id, 'added_at': added_at, 'score': score})

    old_uid = uid

if old_uid is not None:
    for entry in entries:
        print('\t'.join([entry['pid'], entry['title'], entry['tag_names'], curr_user['uid'], entry['node_type'],entry['parent_id'], entry['abs_parent_id'], entry['added_at'], entry['score'],curr_user['reputation'], curr_user['gold'], curr_user['silver'], curr_user['bronze']]))

