import re

login = input("Enter id : ")
password = input("Enter password : ")

log = re.search("^[\w.+\-]+@gmail\.com$",login)
passw = re.search(".{8,}$",password) 

if(log):
    if(passw):
        print("Successfully Login!")
    else:
        print("Password is wrong!")

else:
    print("Email is not vaild")