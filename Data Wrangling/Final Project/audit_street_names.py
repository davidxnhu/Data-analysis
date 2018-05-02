import xml.etree.cElementTree as ET
from collections import defaultdict
import re

OSM_FILE= "D:/Github/data analysis/data wrangling with MongoDB/final_project/singapore.osm"

def audit(osmfile):
    osm_file=open(osmfile,'r')
    street_types=defaultdict(set)

    for event,elem in ET.iterparse(osm_file,events=('start',)):
        if elem.tag=='node' or elem.tag=='way':
            for tag in elem.iter('tag'):
                if is_street_name(tag):
                    audit_street_type(street_types,tag.attrib['v'])
    osm_file.close()
    return street_types

def is_street_name(tag):
    return tag.attrib['k']=='addr:street'

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Alley","Plaza","Commons","Broadway","Expressway","Terrace","Center","Circle",
            "Crescent","Highway","Way","Walk","View","Quay","Park","Hill","Link","Tiga","Close",
            "Sultan","Vale","Green","Loop","Gate","Turn","North","South","West","East",
            "Point","Gardens","Central","Heights"]

def audit_street_type(street_types,street_name):
    '''
    Audit the type of the street name and add it to a street_type set
    '''

    m=street_type_re.search(street_name)
    if m:
        street_type=m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

st_types = audit(OSM_FILE)

print st_types
