import os
from selenium import webdriver
import time


current_dir = os.path.abspath(os.path.dirname(__file__))
# получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')
# добавляем к этому пути имя файла



try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/file_input.html')

    inp1 = browser.find_element_by_name("firstname")
    inp1.send_keys('Ivan')
    inp2 = browser.find_element_by_name("lastname")
    inp2.send_keys('Petrov')
    inp3 = browser.find_element_by_name("email")
    inp3.send_keys('IvanPtrov@mail.ru')

    inp4 = browser.find_element_by_id('file')
    inp4 = browser.find_element_by_css_selector("[type='file']")
    inp4.send_keys(file_path)
    # добавляем наш файл.тхт в элемент на странице

    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(10)
    browser.quit()