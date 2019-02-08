# Automating facebook login using selenium webdriver

from selenium import webdriver 
from time import sleep 
  
u_name=input('Enter your Email:')  
pwd=input('Enter your Password:')  
  
driver = webdriver.Chrome() 
driver.get('https://www.facebook.com/') 
sleep(1) 
  
u_box = driver.find_element_by_id('email') 
u_box.send_keys(u_name) 
sleep(1) 
  
pwd_box = driver.find_element_by_id('pass') 
pwd_box.send_keys(pwd) 
  
login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 
  
print ("Done") 
input('Press anything to quit') 
driver.quit() 
