#
#  Date:  March 25, 2020
#  File:  requests-xml-demo.py
#  Auth:  monica@utk.edu
#  Desc:  Demonstrates parsing XML retrieved directly through an http request
#

import requests
import xml.etree.ElementTree as ET
import xml.dom.minidom  # has a nice feature for making XML pretty

r = requests.get("http://kitty.ninja/demo1.xml")
rcontent = ET.fromstring(r.content) # plug the returned XML content straight into ElementTree
mini_dom = xml.dom.minidom.parseString(r.text) # parse the string response content into an xml dom object
print(mini_dom.toprettyxml()) # all so you can print it out or write it out nicely  ;)
print("\nBY ELEMENT\n")
for elem in rcontent: # for every child node within root (cookies, pies)
  print(elem.tag) # print the element name. This first level of child nodes also has no text
  for subelement in elem: # for all the subelements in the next level down
    print(subelement.tag, subelement.text) # print the tag and the text, since these have text