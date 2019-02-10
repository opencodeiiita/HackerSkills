from selenium import webdriver
import time

username = 'fb_email@email.com'
password = 'fb_password'

browser = webbrowser.Chrome("/Users/vishvajeet/Downloads/chromedriver")

browser.get(https://www.facebook.com/)

browser.find_element_by_id('email').send_keys(username)
browser.find_element_by_id('pass').send_keys(password)

time.sleep(5)

browser.find_element_by_id('loginbutton').click()
