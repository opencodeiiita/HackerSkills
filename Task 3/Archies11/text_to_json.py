from bs4 import BeautifulSoup
import requests
import json

page = requests.get('https://inshorts.com/en/read/')

soup = BeautifulSoup(page.text, 'html.parser')

title = soup.findAll('span', attrs={'itemprop': 'headline'})
body = soup.findAll('div', attrs={'class': 'news-card-content'})
image = soup.findAll('div', attrs={'class': 'news-card-image'})

with open('result.json', mode='w') as f:
    json.dump([],f)

data = []

for length in range(0, len(title)):
    
    with open('result.json', mode='w') as f:
        
        this_news = {'Headline': title[length].text, 
                     'Content': str(body[length].text.splitlines()), 
                     'Image Url': str(image[length])}
        
        data.append(this_news)
        json.dump(data,f)
