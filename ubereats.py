import csv
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
import json

urls = []
city_names = []
data = {}

driver = webdriver.Chrome()
driver.get("https://ubereats.com/toronto/")

restaurant_url = driver.find_elements_by_xpath("//a[contains(@href,'en-CA/toronto/food-delivery')]/*")
lenOfPage = driver.execute_script("var lenOfPage=document.body.scrollHeight;return lenOfPage;")
current_position = 1000

ru = restaurant_url

while current_position < lenOfPage:
	driver.execute_script("window.scrollTo(0, " + str(current_position)+ ")")
	restaurant_url = driver.find_elements_by_xpath("//a[contains(@href,'en-CA/toronto/food-delivery')]/*")
	time.sleep(5)
	for j in restaurant_url:
		try:
			ru.append(i)
		except:
			pass
	current_position = current_position + 1000

resurl = set(ru)

for count, element in enumerate(resurl):
	print(element.text.split("\n")[0])
	print(element.find_element_by_xpath("..").get_attribute('href'))
	print('================================')

with open('ubereats1.json', 'w') as fp:
	json.dump(data, fp)