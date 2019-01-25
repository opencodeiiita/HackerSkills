from requests import get
from bs4 import BeautifulSoup
import json

link = 'https://inshorts.com/en/read/'

r = get(link)

soup = BeautifulSoup(r.content, 'html.parser')

div = soup.findAll('span', attrs={'itemprop': 'headline'})
image = soup.findAll('div', attrs={'class': 'news-card-image'})
con = soup.findAll('div', attrs={'class': 'news-card-content'})

with open('collection.json', mode='w') as f:
    json.dump([],f)

feeds = []

for length in range(0, len(div)):
    with open('collection.json', mode='w') as f:
        entry = {'heading': div[length].text, 'content': str(con[length].text.splitlines()[-5]), 'image': str(image[length]['style'][23:-2])}
        feeds.append(entry)
        json.dump(feeds,f)