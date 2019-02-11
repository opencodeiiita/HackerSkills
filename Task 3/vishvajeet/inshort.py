import urllib.request
from bs4 import BeautifulSoup
import json
import requests

url = " https://inshorts.com/en/read/"

request = urllib.request.Request(url)
html = urllib.request.urlopen(request).read()
soup = BeautifulSoup(html,'html.parser')


title = soup.findAll('span', attrs = {'itemprop':'headline'}) 
image = soup.findAll('div',attrs = {'class' : 'news-card-image'})
content = soup.findAll('div', attrs = {'itemprop':'articleBody'}) 


extracted_records = []

for data in zip(title,content,image):
    record={'Title':data[0].text,
           'Image url':data[1].text,
            'Content':data[2]['style'].split("url('")[1].split("')")[0],
        }

extracted_records.append(record)

with open('data.json', 'w') as outfile:
  json.dump(extracted_records, outfile, indent=4)
