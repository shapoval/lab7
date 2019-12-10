import time
import math
from selenium import webdriver
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/execute_script.html"
driver = webdriver.Chrome()
driver.get(link)
x_element = driver.find_element_by_id("input_value").text
x = x_element
y = calc(x)
input1 = driver.find_element_by_id('answer')
input1.send_keys(y)
option1 = driver.find_element_by_id("robotCheckbox")
option1.click()
option3 = driver.find_element_by_tag_name('button')
driver.execute_script("return arguments[0].scrollIntoView(true);", option3)
option2 = driver.find_element_by_css_selector("[for='robotsRule']")
option2.click()
option3.submit()
