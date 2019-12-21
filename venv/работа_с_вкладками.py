
"""
    browser.switch_to.window(window_name)

    # Чтобы узнать имя новой вкладки, нужно использовать метод window_handles,
    # который возвращает массив имён всех вкладок.
    # Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
    new_window = browser.window_handles[1]

    # Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
    first_window = browser.window_handles[0]
"""

from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    butt = browser.find_element_by_css_selector('.trollface').click()

    new_window = browser.window_handles[1]
    # first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id('input_value').text
    input_value = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(input_value)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()


finally:
    time.sleep(10)
    browser.quit()
