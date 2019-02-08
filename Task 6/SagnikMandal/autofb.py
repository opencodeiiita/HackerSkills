from selenium import webdriver
# Change location of webdriver accordingly
# Works only in Facebook..For other websites we need to change the id's

driver_chrome = webdriver.Chrome('C:/Users/ok/Downloads/chromedriver_win32/chromedriver')
driver_chrome.get('https://www.facebook.com/')

fill_email = driver_chrome.find_element_by_id('email')
fill_email.send_keys('Enter_email')

fill_password = driver_chrome.find_element_by_id('pass')
fill_password.send_keys('password')

login_button = driver_chrome.find_element_by_id('loginbutton')
login_button.click()
