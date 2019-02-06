from selenium import webdriver

drive = webdriver.Chrome('C:\Users\Archisha Baranwal\Downloads\chromedriver_win32')

drive.get('https://www.facebook.com/')

emailid='email_address'

password='password'

drive.find_element_by_id('email').send_keys(emailid)

drive.find_element_by_id('pass').send_keys(password)

submitbtn =find_element_by_id('loginbutton')

submitbtn.click()
