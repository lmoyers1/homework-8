import requests
import xml.etree.ElementTree as ET
import logging
import datetime

logging.basicConfig(filename='hw8_log' + datetime.datetime.utcnow().strftime("%d%b%Y_%Hh%Mm") + '.log', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO)

with open('hw8-input.txt') as f:  # using with automatically closes the file so you don't have to remember to close it yourself
  url_data = f.readlines()  # this is a LIST
  count = 0
#  while count < len(url_data):
  while count < 1:
    clean_url = str.strip(url_data[count])  # strip the URL and save as clean_url
    print("Now attempting to get data at: ", clean_url)
    r = requests.get(clean_url)  # attempt to retrieve the URL
    # check returned status_code, log and print appropriate message
    if r.status_code == 200:
      logging.info("Status Code: {}, URL {} accessible".format(r.status_code,r.url))
      print(r.status_code,"- Successfully retrieved {}".format(r.url))
      # proceed with getting the XML
      tree = ET.parse(r.text)
      root = tree.getroot()
    elif r.status_code == 404:
      logging.error("Status Code: {}, URL {} Not Found".format(r.status_code,r.url))
      print(r.status_code,"- Resource not found for {}".format(r.url))
    elif r.status_code == 500:
      logging.error("Status Code: {}, Internal Server Error".format(r.status_code))
      print(r.status_code,"- Internal Server Error attempting to retrieve {}".format(clean_url))
    elif r.status_code == 503:
      logging.error("Status Code: {}, Service Unavailable".format(r.status_code))
      print('Too much server traffic, wait 20 minutes and try again.')
    else:
      logging.error(r.status_code,"requires further investigation - something went wrong.")
      print("Something went wrong in trying to retrieve the URL {}".format(clean_url))

    count += 1
