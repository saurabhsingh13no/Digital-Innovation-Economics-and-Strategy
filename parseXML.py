import xmltodict, json
import sys
from bs4 import BeautifulSoup

class Wos():

    def __init__(self):
        pass

    def convertXMLToJson(self,contents):
        o = xmltodict.parse(contents)
        return json.dumps(o)


def main():
    file = "./recordForAbrahms"
    infile = open(file)
    contents = infile.read()
    client=Wos()
    json=client.convertXMLToJson(contents)
    print (json)



if __name__ == '__main__':
    main()









