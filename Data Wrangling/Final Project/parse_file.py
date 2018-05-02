import xml.etree.cElementTree as ET

def count_tags(filename):
        
    result={}
    osm_file=open(filename,'r')
    for event,elem in ET.iterparse(osm_file):
        if elem.tag in result:
            result[elem.tag]+=1
        else:
            result[elem.tag]=1
    
    return result

OSM_FILE= "D:/Github/data analysis/data wrangling with MongoDB/final_project/singapore.osm"

result=count_tags(OSM_FILE)
print "The number of different type of tag in the file is: \n"
print result
