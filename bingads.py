from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from decouple import config

BING_USERNAME = config('BING_USERNAME')
BING_PASSWORD = config('BING_PASSWORD')

PATH = '/Users/karimwolbert/Desktop/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://ads.microsoft.com/?mkt=de-de')

username = driver.find_element_by_id('LoginModel_Username')
username.send_keys(BING_USERNAME)
username.send_keys(Keys.RETURN)
time.sleep(3)
password = driver.find_element_by_xpath('//*[@id="i0118"]')
password.send_keys(BING_PASSWORD)
password.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()