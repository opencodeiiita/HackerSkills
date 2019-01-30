from selenium import webdriver

browser = webdriver.Chrome('/home/jaggu/Downloads/chromedriver')
browser.get('https://www.facebook.com/')

fill_email = browser.find_element_by_id('email')
fill_email.send_keys('Enter_email')

fill_password = browser.find_element_by_id('pass')
fill_password.send_keys('password')

password_btn = browser.find_element_by_id('loginbutton')
password_btn.click()