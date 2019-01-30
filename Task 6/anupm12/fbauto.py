# requirements
# install selenium
# download browser driver
from selenium import webdriver
import time

username = 'your_email'
password = 'your_password'

url = 'https://www.facebook.com/'

chrome_driver = webdriver.Chrome("C:/Users/Anupam/Downloads/chromedriver_win32/chromedriver(driver file location)")

chrome_driver.get(url)

chrome_driver.find_element_by_id('email').send_keys(username)
chrome_driver.find_element_by_id('pass').send_keys(password)

time.sleep(2)

chrome_driver.find_element_by_id('loginbutton').click()

print ("Script executed successfully") 
input('Press anything to quit') 
chrome_driver.quit() 
print("Finished") 