from requests import get
from bs4 import BeautifulSoup
import json

link = 'https://inshorts.com/en/read/'
p = get(link)
soup = BeautifulSoup(p.content, 'html.parser')

div = soup.findAll('span', attrs={'itemprop': 'headline'})
image = soup.findAll('div', attrs={'class': 'news-card-image'})
content = soup.findAll('div', attrs={'itemprop': 'articleBody'})
with open('collection.json', mode='w') as f:
    json.dump([],f)

news = []
for length in range(0, len(div)):
    with open('data.json', mode='w') as f:
        sum = {'Heading': div[length].text, 'Content': str(content[length].text.splitlines()[-5]), 'Image': str(image[length]['style'][23:-6])}
        feeds.append(sum)
        json.dump(news,f)