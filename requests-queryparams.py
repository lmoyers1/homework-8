#https://ws.pangaea.de/oai/provider?verb=ListRecords&metadataPrefix=oai_dc&from=2020-03-25

import requests
import xml.dom.minidom

baseurl = "https://ws.pangaea.de/oai/provider"
payload = {'verb': 'ListRecords', 'metadataPrefix' : 'oai_dc', 'from': '2020-03-25' }
my_headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url=baseurl, params=payload, headers=my_headers)
print(r.url)
if r.status_code == 200:
  print("Success!")
  mini_dom = xml.dom.minidom.parseString(r.text)  # parse the string response content into an xml dom object
  print(mini_dom.toprettyxml())
elif r.status_code == 503:
  print('Too much server traffic, wait 20 minutes and try again.')
elif r.status_code == 404:
  print("Resource not found")
else:
  print(r.url)
  print("Unknown problem.")