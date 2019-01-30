import requests
import json
from bs4 import BeautifulSoup


response = requests.get('https://inshorts.com/en/read/')
soup = BeautifulSoup(response.text, 'html.parser')

data = []

for news_card in soup.find_all(class_='news-card'):
	news_title = news_card.find('span',attrs={'itemprop':'headline'}).get_text()
	news_content = news_card.find(class_='news-card-content').get_text(strip=True)
	news_image = news_card.find(class_='news-card-image')
	news_image = str(news_image)
	low = news_image.find("url('")
	high = news_image.find("')") 
	url = news_image[low+len("url('"):high]
	store = {"title: ":news_title,"content: ":news_content,"Image: ":url}
	data.append(store)

data = {"data":data}
with open('jsonfile.json', 'w') as outfile:
    json.dump(data, outfile,indent=2)
json_string = json.dumps(data)
