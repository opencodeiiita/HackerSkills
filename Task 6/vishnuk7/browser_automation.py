# this programm only for windows operating system

from selenium import webdriver

username = ''
password = ''

url = 'https://www.facebook.com'

driver = webdriver.Chrome("./chromedriver")

driver.get(url)
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()