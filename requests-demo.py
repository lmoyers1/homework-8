#
#  Date:  March 25, 2020
#  File:  requests-demo.py
#  Auth:  monica@utk.edu
#  Desc:  Demonstrates use of requests, accessing content and headers, and writing content to file
#


import requests

url1 = "http://kitty.ninja" # first url is just the default home page
url2 = "http://kitty.ninja/demo1.xml" # this is the location of an xml file on the server

outputfile = "demo-downloaded.xml"

print("*****  FIRST REQUEST  *****")

r = requests.get(url1) # assign what is returned from GET request to a response object called r
print(r.text) # the message body encoded as text is accessed through this property
print(r.content) # the message body as bytes is accessed this way.



print("\n*****  SECOND REQUEST  *****")
r = requests.get(url2)

##### Demonstrate different ways to access header information
print("\n*****  HEADERS  *****")
rheaders = r.headers # assign the dictionary of values in the header to a variable
print(rheaders)

print("\n*****  HEADERS BY ITERATION *****")
for item in rheaders.items(): # .items() is one more trick for iterating over dictionaries.
  print("{}: {}".format(item[0], item[1])) # each item of key-value pairs returned as tuple, so access by index

print("\n*****  HEADERS BY KEY  *****")
print("Date: " + rheaders['Date'])
print("Date: " + rheaders['Server'])


print("\nNow writing the contents of the request to file.")
# write the retrieved content to a file
with open(outputfile, 'wb') as f: # notice use of wb and r.content- why do you think we might want to stick to bytes?
  f.write(r.content)