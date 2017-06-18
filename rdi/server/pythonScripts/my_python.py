#!/usr/bin/env python
import web
import xmltodict, json
import xml.etree.ElementTree as ET

tree = ET.parse('user_data.xml')
root = tree.getroot()

urls = (
    '/users', 'list_users',
    '/users/(.*)', 'get_user'
)

app = web.application(urls, globals())

class list_users:        
    def GET(self):
        output = 'users:[';
        for child in root:
                    print ('child', child.tag, child.attrib)
                    output += str(child.attrib) + ','
        output += ']';
        return output

class get_user:

    def convertXMLToJson(self,contents):
        o = xmltodict.parse(contents)
        return json.dumps(o)

    def fetchJson(self):
        file = "../../../recordForAbrahms"
        infile = open(file)
        contents = infile.read()
        json = self.convertXMLToJson(contents)
        return json

    def GET(self, user):
        return self.fetchJson()

if __name__ == "__main__":
    app.run()