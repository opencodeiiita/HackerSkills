import requests
import json
import re
from bs4 import BeautifulSoup
url = "https://inshorts.com/en/read/"
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

# Finds all the headlines(Title) of the news and stores them in the title_list
titles = soup.findAll(class_ = 'clickable')
title_list = []
for item in titles:
    line =item.find("span" , {"itemprop" : "headline"})
    if(line):
        x = line.text
        title_list.append(x)

# Finds the content associated with each news article
content = soup.findAll('div',{"itemprop" : "articleBody"})
content_list = []
for items in content :
    content_list.append(items.text)

# Finding clean URL and storing in url_list
image_url = soup.findAll('div',{"class" : "news-card-image"})
url_list = []
for items in image_url:
    clean_url = items['style']
    clean_url = re.sub(r"background-image: url","",clean_url)
    clean_url = re.sub(r"[()'']", "", clean_url)
    url_list.append(clean_url)
    
# Creating a list to store all the data in json format
item_list = []
for i in range(25):
    data = {
        "Title" : title_list[i],
        "Content" : content_list[i],
        "Image_Url" : url_list[i]
    }
    item_list.append(data)
    with open('data.json', 'a') as outfile:
        json.dump(data, outfile, indent = 4)
