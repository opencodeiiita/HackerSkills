from bs4 import BeautifulSoup
import json
import requests

link = 'https://inshorts.com/en/read/'
r = requests.get(link)

soup = BeautifulSoup(r.content, "html.parser")
title = soup.findAll('span', attrs = {'itemprop':'headline'}) 
image = soup.findAll('div',attrs = {'class' : 'news-card-image'})
content = soup.findAll('div', attrs = {'itemprop':'articleBody'}) 

mydictlist = []

for data in zip(title,content,image):
    mydictlist.append({'title':data[0].text,'Content':data[2]['style'].split("url('")[1].split("')")[0],'Image url':data[1].text})

with open('data.json', 'w+') as outfile:
        json.dump(mydictlist,outfile)
