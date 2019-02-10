import re 
email_id = input("Enter your email id : ")
pwd = input("Enter password : ")

#matches for @gmail.com at the last
if re.search(r'@gmail.com$',email_id):
    print("Valid mail id \n")
else :
    print("Invalid mail id")

if len(pwd)>8 :
    print("Password is valid ")
else :
    print("Password is invalid")
