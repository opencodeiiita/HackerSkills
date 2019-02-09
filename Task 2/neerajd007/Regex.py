import re

email_id = raw_input("Enter e-mail id to login:")
password = raw_input("Enter the password:")

Isemail = re.search("^[\w.+\-]+@gmail\.com$", email_id)
Ispassword = re.search(".{8,}$", password)

if(Isemail):
	if(Ispassword):
		print("Login Successfull")
	else:
		print("Password should be of 8 characters")

else:
	print("Invalid e-mail id")
