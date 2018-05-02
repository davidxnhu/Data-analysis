import csv

def add_unique_id(filename,newfilename,id):
    with open(filename,'rb') as infile, open(newfilename,'wb') as outfile:
        reader=csv.reader(infile)
        writer=csv.writer(outfile,delimiter=',')
        writer.writerow([id]+next(reader))
        writer.writerows([i]+row for i,row in enumerate(reader,1))

add_unique_id('nodes_tags.csv','nodes_tags_id.csv','NodetagId')
add_unique_id('ways_nodes.csv','ways_nodes_id.csv','WaynodeId')
add_unique_id('ways_tags.csv','ways_tags_id.csv','WaytagId')

def skip_header(filename,newfilename):
    '''remove the header line from the file and output to a new file'''
    with open(filename,'rb') as infile, open(newfilename,'wb') as outfile:
        reader=csv.reader(infile)
        reader.next()
        writer=csv.writer(outfile)
        for line in reader:
            writer.writerow(line)

skip_header("nodes.csv","nodes_noheader.csv")
skip_header("ways.csv","ways_noheader.csv")
skip_header("nodes_tags_id.csv","nodes_tags_noheader.csv")
skip_header("ways_nodes_id.csv","ways_nodes_noheader.csv")
skip_header("ways_tags_id.csv","ways_tags_noheader.csv")
