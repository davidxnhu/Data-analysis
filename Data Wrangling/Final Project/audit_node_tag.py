import xml.etree.cElementTree as ET
import re



lower = re.compile(r'^([a-z]|_|\d)*$', re.IGNORECASE)
lower_colon = re.compile(r'^([a-z]|_|\d)*:([a-z]|_|\d)*$', re.IGNORECASE)
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]', re.IGNORECASE)

def audit_tags(osmfile):
    '''
    Audit an osmfile and return sets of node tag keys, node tag values, way tag keys,
    and way tag values
    '''

    osm_file=open(osmfile,'r')
    node_tags_keys,node_tags_values,way_tags_keys,way_tags_values=set(),set(),set(),set()

    for event,elem in ET.iterparse(osm_file,events=("start",)): #too large to load into a tree
        if elem.tag=="node":
            for tag in elem.iter("tag"):
              node_tags_keys.add(tag.attrib['k'])
              node_tags_values.add(tag.attrib['v'])
        elif elem.tag=="way":
            for tag in elem.iter("tag"):
              way_tags_keys.add(tag.attrib['k'])
              way_tags_values.add(tag.attrib['v'])
    
    osm_file.close()
    return node_tags_keys,node_tags_values,way_tags_keys,way_tags_values

OSM_FILE= "D:/Github/data analysis/data wrangling with MongoDB/final_project/singapore.osm"
NEW_OSM_FILE = "D:/Github/data analysis/data wrangling with MongoDB/final_project/singapore_clean_node_tag.osm"

node_tags_keys,node_tags_values,way_tag_keys,way_tag_values=audit_tags(NEW_OSM_FILE)

def tag_keys(tag_keys_set):
    '''
    Return sets of different types of the keys in the given set
    '''

    lower_keys,lower_colon_keys,problemchars_keys,others_keys=set(),set(),set(),set()

    for key in tag_keys_set:
        if lower.search(key):
            lower_keys.add(key)
        elif lower_colon.search(key):
            lower_colon_keys.add(key)
        elif problemchars.search(key):
            problemchars_keys.add(key)
        else:
            others_keys.add(key)
    
    return lower_keys,lower_colon_keys,problemchars_keys,others_keys

node_lower_keys,node_lower_colon_keys,node_problemchars_keys,node_others_keys = tag_keys(node_tags_keys)
node_key_types = {"total": len(node_tags_keys),"lower":len(node_lower_keys),"lower colon":len(node_lower_colon_keys),"problemchars":len(node_problemchars_keys),"others":len(node_others_keys)}

print "The number of keys for each type is:"
print node_key_types

'''uncomment the print lines below for tag keys of each category'''

#print "node tag keys containg lower case letters" 
#print node_lower_keys

#print "node tag keys containing 1 colon" 
#print node_lower_colon_keys

#print "node tag keys with problem chars" 
#print node_problemchars_keys

print "other node tag keys" 
print node_others_keys
