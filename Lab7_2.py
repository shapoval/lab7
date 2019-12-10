import time
import math
from selenium import webdriver
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/get_attribute.html"
driver = webdriver.Chrome()
driver.get(link)
people_radio = driver.find_element_by_id("treasure")
x_element = people_radio.get_attribute("valuex")
x = x_element
y = calc(x)
input1 = driver.find_element_by_id('answer')
input1.send_keys(y)
option1 = driver.find_element_by_id("robotCheckbox")
option1.click()
option2 = driver.find_element_by_id("robotsRule")
option2.click()

option3 = driver.find_element_by_tag_name('button')
option3.submit()
