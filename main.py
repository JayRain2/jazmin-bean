from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.google.com')

assert 'Google' in driver.title

elem = driver.find_element(By.NAME, 'q')

elem.send_keys('Jazmin Bean')
elem.send_keys(Keys.RETURN)

assert 'No resulds found.' not in driver.page_source

sleep(1)

button = driver.find_element(By.XPATH,"//*[contains(text(), 'Images')]")

button.click()

sleep(2)

while True:
	sleep(1)
	html = driver.find_element(By.TAG_NAME, 'html')
	html.send_keys(Keys.PAGE_DOWN)
