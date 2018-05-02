import xml.etree.cElementTree as ET

OSM_FILE= "D:/Github/data analysis/data wrangling with MongoDB/final_project/singapore.osm"

def audit_prob_attrib(osmfile,key):
    """Return the element id, uid, and tag.attrib of a given key"""
    osm_file = open(osmfile, "r")
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node": 
            for tag in elem.iter('tag'):
                if tag.attrib['k'] == key:
                    print (elem.attrib['id'],elem.attrib['uid'],elem.attrib['lat'],elem.attrib['lon'],tag.attrib)
    osm_file.close()

def get_tags(osmfile,node_id):
    """Return the tag.attrib of a given id"""
    osm_file = open(osmfile, "r")
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node": 
            if elem.attrib['id'] == node_id:
                for tag in elem.iter('tag'):
                    print tag.attrib
    osm_file.close()


print "node id, user id, tags containing 'FIXME':"
audit_prob_attrib(OSM_FILE,'FIXME')
print "node id, user id, tags containing 'fixme':"
audit_prob_attrib(OSM_FILE,'fixme')

