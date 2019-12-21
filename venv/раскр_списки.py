from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# http://suninjuly.github.io/selects1.html
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects2.html')

    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    a,b = int(x), int(y)
    res = a + b
    result = str(res)

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(result)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
