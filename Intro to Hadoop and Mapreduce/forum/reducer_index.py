#! /usr/bin/python

import sys

pre_word=None
nodes=[]


for line in sys.stdin:
    data=line.strip().split("\t")
    if len(data)!=2:
        continue
    
    this_word,node_id=data
    if pre_word and pre_word!=this_word:
        print pre_word, "\t", sorted(nodes), "\t", len(nodes)
        nodes=[]

    pre_word=this_word
    nodes.append(int(node_id))

if pre_word:
    print pre_word, "\t", sorted(nodes), "\t", len(nodes)    
