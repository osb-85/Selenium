from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://SunInJuly.github.io/execute_script.html')
    x = browser.find_element_by_id('input_value').text
    input_value = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(input_value)

    rch = browser.find_element_by_id('robotCheckbox')
    rch.click()

    # Так в скобках указывается JS код который надо выполнить
    browser.execute_script('window.scrollBy(0, 200);')

    rrr = browser.find_element_by_id('robotsRule')
    rrr.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()


finally:
    time.sleep(10)
    browser.quit()
