import requests
import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

    
location=input("enter location")
description=input("description")

URL = "https://jobs.github.com/positions.json?description="+description+"&location=san+"+location

r = requests.get(url = URL)

data = r.json() 

for i in range(3):
    title=data[i]['title']
    description=remove_tags(data[i]['description'])
    link=data[i]['url']
    print("title: "+title)
    print("description: "+description)
    print("link: "+link)
    print("\n")


