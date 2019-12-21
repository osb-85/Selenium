from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    x = browser.find_element_by_id('treasure').get_attribute('valuex')
    input_value = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(input_value)

    rch = browser.find_element_by_id('robotCheckbox')
    rch.click()

    rrr = browser.find_element_by_id('robotsRule')
    rrr.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()


finally:
    time.sleep(10)
    browser.quit()