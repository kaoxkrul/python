#!/usr/bin/python
# Python page scraper for http://malc0de.com/database
# Rob Krul - robertkrul27@gmail.com
# Scrapes values from malcode.com/database and saves data into formatted csv file
# Tested on Python 2.7.3 on Mac OS X 10.8.2

import csv
import datetime
import requests
import urllib2
import string
import time
import html5lib                 #no other parsers worked as well
from bs4 import BeautifulSoup

# Format the filename with timestamp
utc_datetime = datetime.datetime.utcnow()    
formatted_date = utc_datetime.strftime("%Y-%m-%d-%H%M")
filename = 'Malcode-Culled-Product-' + formatted_date +'.csv'

# Start the soup and parse the table
response = urllib2.urlopen('http://malc0de.com/database/')
html = response.read()
soup = BeautifulSoup(html)
table = soup.find("table", {"class" : "prettytable"})

# Open the local csv file and format the cells
file = open(filename, "w")
file.write("Discovery Date, File Name, IP Address, Country Code, ASN, ASN Name, MD5")
file.write("\n")

# For loop that scrapes the data off of the html page and into array
for row in table.findAll('tr') [1:]:
   col=row.findAll('td')

   date = col[0].string
   domain = col[1].string
   ip = col[2].string
   cc = col[3].string
   asn = col[4].string
   sys_name = col[5].string
   md5 = col[6].string

   format_ip = ip.replace(".", "{.}")

# Write the scraped data to the csv file
   file = csv.writer(open(filename, "a"))
   file.writerow([date, domain, format_ip, cc, asn, sys_name, md5])

