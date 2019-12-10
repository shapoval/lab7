import time
import math
from selenium import webdriver
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/math.html"
driver = webdriver.Chrome()
driver.get(link)
x_element = driver.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
inputs = driver.find_element_by_id('answer')
inputs.send_keys(y)
option = driver.find_element_by_css_selector("[for='robotCheckbox']")
option.click()
option1 = driver.find_element_by_css_selector("[for='robotsRule']")
option1.click()
option2 = driver.find_element_by_tag_name('button')
option.submit()