import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/explicit_wait2.html"
driver = webdriver.Chrome()
driver.get(link)

button = WebDriverWait(driver, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

option3 = driver.find_element_by_id('book')
option3.click()

x_element = driver.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
input1 = driver.find_element_by_id('answer')
input1.send_keys(y)

option4 = driver.find_element_by_id('solve')
option4.submit()