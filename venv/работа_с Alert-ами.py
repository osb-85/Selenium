
alert = browser.switch_to.alert
alert.accept()

# Чтобы получить текст из alert, используйте свойство text объекта alert:
alert = browser.switch_to.alert
alert_text = alert.text

# Другой вариант модального окна, который предлагает пользователю выбор
# согласиться с сообщением или отказаться от него, называется confirm.
# Для переключения на окно confirm используется та же команда, что и в случае с alert:

confirm = browser.switch_to.alert
confirm.accept()

# Для confirm-окон можно использовать следующий метод для отказа:
confirm = browser.switch_to.alert
confirm.dismiss()

# Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста.
# Чтобы ввести текст, используйте метод send_keys():

prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()

