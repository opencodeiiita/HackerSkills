from selenium import webdriver

username = 'username'
password = 'password'

# Telling the webdriver to go to once it has opened chrome
url = 'https://www.facebook.com/'

# Telling webdriver to where to find the chrome driver
driver = webdriver.Chrome("C:/Users/devgu/Downloads/chromedriver")

#Telling driver to get the url
driver.get(url)

#finding elements by id on the facebook login page and using send_keys to
#send the username and password stored
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)

#click also included in selenium package
driver.find_element_by_id('loginbutton').click()
