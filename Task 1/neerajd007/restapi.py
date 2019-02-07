import requests, re, json

print("Enter the description of the job:")
desc=raw_input()
print("Enter the location of the job:")
location=raw_input()
resp = requests.get("https://jobs.github.com/positions.json?description"+desc+"&loaction="+location)


if resp:
	for data in resp:
		print("Title :" + data+"\n")
		cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', data)
        print("Description :" + cleantext +"\n")
        print("Url :" + data+"\n")
        print("-----------------------")
		

else:
	print("No jobs found")