from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user=input("enter your email")
pwd=input("enter your password")
driver = webdriver.Chrome()

driver.get("http://www.facebook.com")

log = driver.find_element_by_id("email")
log.send_keys(user)
log = driver.find_element_by_id("pass")
log.send_keys(pwd)
log.send_keys(Keys.RETURN)
