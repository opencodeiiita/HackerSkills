import re
email=input()
pswrd=input()
emailregex=re.compile(r'@+[gmail]+(\.[com])')
passregex=re.compile(r'\w{8,}')
a=emailregex.search(email)
b=passregex.search(pswrd)
if a==None:
    print("Invalid Email")
else:
    print("Valid Email")
if b==None:
    print("Invalid Password")
else:
    print("Valid Password")
