import math
from selenium import webdriver
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x,y):
  return str((int(x)+int(y)))

x = browser.find_element_by_id("num1").text
y = browser.find_element_by_id("num2").text


z = calc(x,y)

browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("[value='" + z + "']").click()

option3 = browser.find_element_by_tag_name('button')
option3.submit()