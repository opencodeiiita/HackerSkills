import re

userid = input("Enter id : ")
password = input("Enter password : ")

user = re.search("^[\w.+\-]+@gmail\.com$",userid)
key = re.search(".{8,}$",password)

if user:
    if key:
        print(" Login Successfully !")
    else:
        print("You Entered wrong password")

else:
    print("Email is invaild")
