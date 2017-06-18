from wos import WosClient
import wos.utils
import xml.etree.ElementTree as ET

file="./reocrdForAbrahms, Max"
tree = ET.parse(file)
root = tree.getroot()

for child in root:
    print (child.tag, child.attrib)

for neighbor in root.findall('count'):
    print (neighbor.attrib)
