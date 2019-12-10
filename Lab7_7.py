import time
import math
from selenium import webdriver
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/redirect_accept.html"
driver = webdriver.Chrome()
driver.get(link)
option3 = driver.find_element_by_tag_name('button')
option3.submit()
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)
x_element = driver.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
input1 = driver.find_element_by_id('answer')
input1.send_keys(y)
option3 = driver.find_element_by_tag_name('button')
option3.submit()