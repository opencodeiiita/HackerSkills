from bs4 import BeautifulSoup
import requests
import re
import json 

url = 'https://inshorts.com/en/read/'

data = requests.get(url)
soup = BeautifulSoup(data.content, "html.parser")


#**************** Headlines ****************************

headlines = soup.find_all('div',class_=["news-card-title news-right-box"])
titles = []

for headline in headlines:
    head = headline.find('span',attrs={"itemprop":"headline"}).string
    titles.append(head)

#**************** Articles ******************************
articles = soup.find_all('div',class_=["news-card-content news-right-box"])
content = []

for article in articles:
    material = article.find('div',attrs={"itemprop":"articleBody"}).text
    content.append(material)

#**************** Urls **********************************
    
images = soup.find_all('div',class_=["news-card-image"])
img_urls = []

for image in images:
    img_url = image['style']
    img_url = re.sub(r"background-image: url","",img_url)
    img_url = re.sub(r"[()'']","",img_url)
    img_urls.append(img_url)


req_data = []

for i in range(20):
    d = {
        "Title" : titles[i],
        "Content" : content[i],
        "Image_Url" : img_urls[i]
    }
    req_data.append(d)

with open('inshorts.json', 'a') as file:
    json.dump(req_data, file, indent = 5)