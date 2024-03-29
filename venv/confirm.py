from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    button = browser.find_element_by_css_selector("[type='submit']").click()

    confirm = browser.switch_to_alert()
    confirm.accept()

    x = browser.find_element_by_id('input_value').text
    input_value = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(input_value)

    but = browser.find_element_by_css_selector('button.btn')
    but.click()

finally:
    time.sleep(5)
    browser.quit()