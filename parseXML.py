import xmltodict, json
import sys
from bs4 import BeautifulSoup
from wos import WosClient
import wos.utils

class Wos():

    def __init__(self):
        pass

    def convertXMLToJson(self,contents):
        o = xmltodict.parse(contents)
        return json.dumps(o)


def main():
    user='Ahmed, Amal'
    # with WosClient(user='singh.saurab@husky.neu.edu',
    #                password='Chanchala13.') as  client:
    #     filename = (wos.utils.query(client, 'AU=%s'), user)
    file = "recordForAbrahms"
    infile = open(file)
    contents = infile.read()
    client=Wos()
    Json=client.convertXMLToJson(contents)
    print (type(json.loads(Json)))



if __name__ == '__main__':
    main()









