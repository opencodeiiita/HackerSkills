# before run this programm please install requests
# pip3 install request

import requests,json
import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext



description = input("Enter the deescription :")
location = input("Enter the location :")



r = requests.get('https://jobs.github.com/positions.json?description=' + description + '&location=' + location)
data = r.json()
if data:
    for i in range(len(data)):
        print(" title : \t" + data[i]['title'] + "\n")
        print(" description: \t" + cleanhtml(data[i]["description"]) + "\n" )
        print(" company_url: \t" + str((data[i]["company_url"])) + "\n")
else:
    print("No Result found :(")