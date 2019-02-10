from selenium import webdriver
import os
driver = webdriver.Chrome("./chromedriver")
driver.get ('https://www.facebook.com/')
email = input("Enter email :\n")
driver.find_element_by_id("email").send_keys(email)
password = input("Enter password :\n")
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_id("loginbutton").click()
