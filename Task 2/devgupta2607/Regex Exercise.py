#Author: devgupta2607

import re

email = input("Email Address : ")
password = input("Password      : ")

checkemail = re.search(r'^.+@gmail\.com$',email)
checkpass = re.search(r'.{8,}$',password)

if checkemail :
    if checkpass:
        print("Login Successful")
    else:
        print("Password is incorrect. Try Again")
else :
    print("Email is not valid. Try Again")
    
