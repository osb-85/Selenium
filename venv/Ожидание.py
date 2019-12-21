"""
    from selenium import webdriver

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text
"""

# Улучшим наш тест с помощью неявных ожиданий.
# добавить одну строчку с методом implicitly wait:

from selenium import webdriver

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

browser.quit()

# Ожидания в Selenium WebDriver
# https://selenium.dev/documentation/en/
# https://selenium-python.readthedocs.io/waits.html
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
# https://stackoverflow.com/questions/15122864/selenium-wait-until-document-is-ready
# https://blog.codeship.com/get-selenium-to-wait-for-page-load/