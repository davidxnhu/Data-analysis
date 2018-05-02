import xml.etree.cElementTree as ET
import re

OSM_FILE= "D:/Github/data analysis/data wrangling with MongoDB/final_project/singapore.osm"
NEW_OSM_FILE = "D:/Github/data analysis/data wrangling with MongoDB/final_project/singapore_cleaned.osm"

def audit(osmfile):
    osm_file=open(osmfile,'r')
    postcodes=set()
    for event,elem in ET.iterparse(osm_file,events=('start',)):
        if elem.tag=='node' or elem.tag=='way':
            for tag in elem.iter('tag'):
                if is_postcode(tag):
                    audit_postcode(postcodes,tag.attrib['v'])
    
    osm_file.close()
    return postcodes

def is_postcode(tag):
    return tag.attrib['k']=='addr:postcode' or tag.attrib['k'] == 'postal_code'

postcode_re = re.compile(r'^\d{6}$')  # postcode is 6-digit in Singapore
def audit_postcode(postcodes,postcode):
    '''
    Audit the format and return unexpected value
    '''
    m=postcode_re.search(postcode)
    if not m:
        postcodes.add(postcode)

postcodes=audit(NEW_OSM_FILE)

print 'unexpected postcodes'
print postcodes


