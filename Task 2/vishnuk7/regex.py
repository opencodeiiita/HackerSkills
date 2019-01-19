import re

login_id = input("Enter the id : ")
password = input("Enter the password : ")

login_check = re.search("^[\w.+\-]+@gmail\.com$",login_id)
password_check = re.search(".{8,}$",password) 

if(login_check):
    if(password_check):
        print("Successfully Login!")
    else:
        print("Password is wrong! At Least 8 characters are required")
else:
    print("Only use gmail account or email is not vaild")

