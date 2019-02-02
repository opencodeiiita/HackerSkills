email=input("enter email  ")
password=input("Enter password  ")
import re  
#the regex is copied from some website.
if re.match('\\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\\"?', email)!=None:
    print("VALID EMAIL")
else:
    print("INVALID EMAIL")

if len(password)>8:
    print("VALID PASSWORD")
else:
    print("INVALID PASSWORD")
