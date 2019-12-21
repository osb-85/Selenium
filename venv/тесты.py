"""Если значение выражения истинно, то в консоли не должно появиться дополнительных сообщений. Выполним:
>>> assert abs(-42) == 42

Если условие не выполнено, то в консоли выводится лог ошибки с названием файла и номером строчки,
в которой произошла ошибка, а также тип ошибки AssertionError:

>>> assert abs(-42) == -42

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError

Простое сообщение AssertionError не очень информативно.
Когда тестов становится много, бывает сложно вспомнить, что именно мы проверяем в данном тесте.
Для добавления дополнительного сообщения можно при вызове assert через запятую написать нужное сообщение,
которое будет выведено в случае ошибки проверки результата:

assert abs(-42) == -42, 'ищем значение'
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AssertionError: ищем значение

def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result, f'expected {expected_result}, got {actual_result}'


для проверки того, что в текущем url содержится строка login:
assert "login" in browser.current_url, # сообщение об ошибке

"""