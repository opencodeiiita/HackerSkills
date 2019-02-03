import requests
import re
import json

collectedData = requests.get("https://jobs.github.com/positions.json?description="+
    input("Enter job description")+"&location="+
    input("Enter job location")).json()

if collectedData:
    for data in collectedData:
        print("Job title :" + data['title']+"\n")
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', data['description'])
        print("Job description :" + cleantext +"\n")
        print("Job URL :" + data['url']+"\n")
else:
    print("Selected type of job is not found")