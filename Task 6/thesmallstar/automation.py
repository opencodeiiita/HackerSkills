
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time

browser = webdriver.Firefox()
browser.get("http:\\outlook.com\website.com") 
time.sleep(10) 
username = browser.find_element_by_id("user_input_id") 
password = browser.find_element_by_id("password_input_id")
username.send_keys("your_username") 
password.send_keys("your_password") 
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()
