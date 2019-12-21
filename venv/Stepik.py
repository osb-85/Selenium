from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/simple_form_find_task.html')
    button = browser.find_element_by_id("submit_button")
    button.click()

finally:
    browser.quit()

