# *************************************************************
#                                                             *
#           INSC 360 Spring 2020, Homework #8                 *
#           File name: hw8.py                                 *
#            Due date: 15 April 2020                          *
#              Author: Laura Moyers                           *
#                                                             *
#  This program fetches XML files of bank customer data off a *
#  server, parses the information, and prints the data off in *
#  a way that is nicely formatted.  INFO/ERROR logging is     *
#  supported, as is exception handling if the target URL is   *
#  inaccessible.                                              *
#                                                             *
# *************************************************************

import requests
import xml.etree.ElementTree as ET
import logging
import datetime

logging.basicConfig(filename='hw8_log' + datetime.datetime.utcnow().strftime("%d%b%Y_%Hh%Mm") + '.log', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, filemode='w')

with open('hw8-input.txt') as f:  # using with automatically closes the file so you don't have to remember to close it yourself
  url_data = f.readlines()  # this is a LIST
  print('FETCHING BANK CUSTOMER DATA')
  logging.info("Begin fetching customer data")
  count = 0
  while count < len(url_data):
    clean_url = str.strip(url_data[count])  # strip the URL and save as clean_url
    print("\n" + "*" * 80)
    print("Now attempting to get data at: {}".format(clean_url))
    logging.info("Now attempting to get data at: {}".format(clean_url))
    r = requests.get(clean_url)  # attempt to retrieve the URL
    # check returned status_code, log and print appropriate message
    if r.status_code == 200:
      logging.info(str(r.status_code) + " - Successfully retrieved {}".format(r.url))
      print(r.status_code,"- Successfully retrieved {}".format(r.url))
      # get XML data and print prettily
      root = ET.fromstring(r.text)  # banking_customers
      for elem in root:  # customer
        for subelement in elem:  # id, name, checking_account, savings_account
          if subelement.tag == "id":
            logging.info("Now processing customer ID {}".format(subelement.text))
          if subelement.tag == "name":
            name = subelement.text
            print("\n",name)
          if subelement.tag == "checking_account":
            print("\tChecking Account: {}".format(subelement.text))
          if subelement.tag == "savings_account":
            print("\tSavings Account: {}".format(subelement.text))
    elif r.status_code == 404:
      logging.error(str(r.status_code) + " - Resource not found for {}".format(r.url))
      print(r.status_code,"- Resource not found for {}".format(r.url))
    else:
      logging.error(str(r.status_code)," - Requires further investigation - something went wrong.")
      print("Something went wrong in trying to retrieve the URL {}.  See log file for information".format(clean_url))

    count += 1
