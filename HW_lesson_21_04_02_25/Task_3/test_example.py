# Task_3
# test_example.py


"""
A test case for functions using the pytest library (full pytest
documentation) with a context manager implementation to return a file
object that can be used in functions.
"""


import pytest
from io import StringIO
from main import test_check  # Імпортуй основну функцію з головного файлу


# Фікстура для створення тестового файлу
@pytest.fixture
def file_obj():
    with open('example.txt', 'r', encoding='utf-8') as file:
        file_content = file.read()
    return StringIO(file_content)


# Тестова функція для перевірки результатів
def test_check_results(file_obj):
    # Очікувані результати (змінити на відповідні значення для `example.txt`)
    expected_lines = 8
    expected_words = 25
    expected_chars = 158

    # Виклик функції та перевірка результатів
    file_obj.seek(0)  # Скидає покажчик на початок файлу
    lines, words, chars = test_check(file_obj)
    assert lines == expected_lines, f"Очікувана кількість рядків:\
        {expected_lines}, отримано: {lines}"
    assert words == expected_words, f"Очікувана кількість слів:\
        {expected_words}, отримано: {words}"
    assert chars == expected_chars, f"Очікувана кількість символів:\
        {expected_chars}, отримано: {chars}"


if __name__ == '__main__':
    pytest.main()
