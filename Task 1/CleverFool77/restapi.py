import requests,re
datas = requests.get("https://jobs.github.com/positions.json?description="+input("enter description")+"&location="+input("enter place")).json()

if datas:
    for data in datas:
        print("Title :" + data['title']+"\n")
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', data['description'])
        print("Desc :" + cleantext +"\n")
        print("Url :" + data['url']+"\n")
        print("+++++++++++++++++++++++++")
else:
    print("your choice is not Found")