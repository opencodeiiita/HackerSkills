from selenium import webdriver

username = '' #add username
password = '' #add password

url = 'https://www.facebook.com'

# https://chromedriver.storage.googleapis.com/index.html?path=2.38/
# download the chromedriver and put into current directory

driver = webdriver.Chrome("./chromedriver")

driver.get(url)
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click() 