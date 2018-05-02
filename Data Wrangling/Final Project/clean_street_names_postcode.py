import xml.etree.cElementTree as ET
import re

OSM_FILE = "D:/Github/data analysis/data wrangling with MongoDB/final_project/singapore_clean_node_tag.osm"  # Replace this with your osm file
NEW_OSM_FILE = "D:/Github/data analysis/data wrangling with MongoDB/final_project/singapore_cleaned.osm"

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Alley","Plaza","Commons","Broadway","Expressway","Terrace","Center","Circle",
            "Crescent","Highway","Way","Walk","View","Quay","Park","Hill","Link","Tiga","Close",
            "Sultan","Vale","Green","Loop","Gate","Turn","North","South","West","East",
            "Point","Gardens","Central","Heights"]
street_mapping = { 
                  "Ave":"Avenue",
                  "Ave.":"Avenue",
                  "Avene":"Avenue",
                  "Aveneu":"Avenue",
                  "ave":"Avenue",
                  "Avebue":"Avenue",
                  "avenue":"Avenue",
                  "Blv.":"Boulevard",
                  "Blvd":"Boulevard",
                  "blvd":"Boulevard",
                  "Broadway.":"Broadway",
                  "Ctr":"Center",
                  "Dr":"Drive",
                  "Pkwy":"Parkway",
                  "Plz":"Plaza",
                  "PARK":"Park",
                  "Rd":"Road",
                  "Rd.":"Road",
                  "road":"Road",
                  "ST":"Street",
                  "St":"Street",
                  "St.":"Street",
                  "Steet":"Street",
                  "Streeet":"Street",
                  "st":"Street",
                  "street":"Street",
                  "terrace":"Terrace"
                  }


def get_element(osm_file,tags=('node','way','relation')):
    '''
    Yield element if it is the right type
    '''
    context=iter(ET.iterparse(osm_file,events=('start','end')))
    _,root=next(context)
    for event,elem in context:
        if event=='end' and elem.tag in tags:
            yield elem
            root.clear()


def clean(filename,newfilename):
    '''
    Create a new file with street names and postcodes cleaned
    '''

    with open(filename,'rb') as infile, open(newfilename,'wb') as outfile:
        outfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        outfile.write('<osm>\n')

        for elem in get_element(infile):
            if elem.tag=='node' or elem.tag=='way':
                if elem.find('tag')!=-1:
                    for tag in elem.iter('tag'):
                        if is_street(tag):
                            tag.attrib['v']=better_name(tag.attrib['v'])

                        elif is_postcode(tag):
                            postcode=tag.attrib['v']
                            new_postcode=better_postcode(postcode)
                            if not new_postcode:
                                elem.remove(tag)
                            else:
                                tag.attrib['v']=new_postcode
            outfile.write(ET.tostring(elem,encoding='utf-8'))

        outfile.write('</osm>\n')

def is_street(tag):
    return tag.attrib['k']=='addr:street'

def is_postcode(tag):
    return tag.attrib['k']=='addr:postcode' or tag.attrib['k'] == 'postal_code'


def better_name(street_name):
    if street_name.find('Jalan')==0:
        return street_name
    elif street_name.find('Jln')==0:
        return 'Jalan'+street_name[3:]
    elif street_name.find('Jl.')==0:
        return 'Jalan'+street_name[3:]
    elif street_name.find('Lorong')==0:
        return street_name
    elif street_name.find('Lor')==0:
        return street_name

    
    m=street_type_re.search(street_name)
    if m:
        pattern=m.group()
        if pattern not in expected and not pattern.isdigit():
            index=street_name.find(pattern)
            try:
                street_name=street_name[:index]+street_mapping[pattern]+street_name[index+len(pattern):]
            except:
                print street_name, "could not find key"
        
    return street_name

def better_postcode(postcode):
    result=postcode.strip()
    if result.find('Singapore')!=0:
        result.replace('Singapore','')
    elif result.find('S')!=0:
        result.replace('S','')


    if result.isdigit() and len(result)==6:
        return result
    else:
        return None


clean(OSM_FILE,NEW_OSM_FILE)    




        
