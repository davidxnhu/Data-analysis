import xml.etree.cElementTree as ET

OSM_FILE = "D:/Github/data analysis/data wrangling with MongoDB/final_project/singapore.osm"  # Replace this with your osm file
NEW_OSM_FILE = "D:/Github/data analysis/data wrangling with MongoDB/final_project/singapore_clean_node_tag.osm"

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
    
def clean_node_tag_keys(filename,newfilename):
    '''
    Create a new xml file with node tag keys and values updated
    '''
    with open(filename,'rb') as infile, open(newfilename,'wb') as outfile:
        outfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        outfile.write('<osm>/n')

        for elem in get_element(infile):
            if elem.tag=='node':
                if elem.find('tag')!=-1:
                    for tag in elem.iter('tag'):
                        if tag.attrib['k']=='FIXME' or tag.attrib['k']=='fixme':
                            elem.remove(tag)
                            if tag.attrib['v']=='continue' or tag.attrib['v']=='continues':
                                ET.SubElement(elem,'tag',{'k':'noexit','v':'yes'})
                            # more values could be clean here

                        elif ' ' in tag.attrib['k']:
                            tag.attrib['k']=convert_key(' ','_',tag.attrib['k'])
                        elif '/' in tag.attrib['k']:
                            tag.attrib['k']=convert_key('/','_',tag.attrib['k'])
                        elif tag.attrib['k'].count(':')>1:
                            tag.attrib['k']=convert_multiple_colon(tag.attrib['k'])
            outfile.write(ET.tostring(elem,encoding='utf-8'))
        
        outfile.write('</osm>')

def convert_key(old_key,new_key,key):
    index=key.find(old_key)
    better_key=key[:index]+new_key+key[index+len(old_key):]
    return better_key

def convert_multiple_colon(key):
    '''
    Only maintain the first colon
    '''
    index=key.find(':')  #index of first colon
    better_key=key[:index+1]+key[index+1:].replace(':','_')
    return better_key


clean_node_tag_keys(OSM_FILE,NEW_OSM_FILE)
