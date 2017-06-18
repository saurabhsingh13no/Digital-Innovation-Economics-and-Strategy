import xmltodict, json
import sys
from bs4 import BeautifulSoup



def convertXMLToJson(contents):
    o = xmltodict.parse(contents)
    return json.dumps(o)



def main():
    file = "./recordForAbrahms"
    infile = open(file)
    contents = infile.read()
    json=convertXMLToJson(contents)
    return json



if __name__ == '__main__':
    main()









