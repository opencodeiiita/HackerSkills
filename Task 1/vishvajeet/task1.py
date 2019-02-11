import requests,re,json

datas = requests.get("https://jobs.github.com/positions.json?description="+input("jobs description")+"&location="+input("Location")).json()

if datas:
    for data in datas:
        print("Job Title :" + data['Jobtitle']+"\n")
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', data['Jobdescription'])
        print("Job Description :" + cleantext +"\n")
        print("Job Url :" + data['url']+"\n")
        print("Github Jobs using REST API.")

else:
    print("Required job not found")
