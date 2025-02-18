# Task_2
"""
    Take your implementation of the context manager class from Task 1 and write
    tests for it. Try to cover as many use cases as you can, positive ones when
    a file exists and everything works as designed. And also, write tests when
    your class raises errors or you have errors in the runtime context suite.
"""


import unittest
import os
from Task_1 import CustomFile  # Клас зберігається у файлі Task_1.py


class TestCustomFile(unittest.TestCase):

    def setUp(self):
        """
        Підготовка до тестів: створення тестового файлу.
        """
        self.filename = 'test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Initial content')

    def tearDown(self):
        """
        Прибирання після тестів: видалення тестового файлу
        """
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_write_and_read(self):
        """
        Тестування запису та читання даних.
        """
        with CustomFile(self.filename, 'w') as f:
            f.write('Мене звати Сергій')

        with CustomFile(self.filename, 'r') as f:
            content = f.read()
            self.assertEqual(content, 'Мене звати Сергій')

    def test_read_counter(self):
        """
        Тестування лічильника читань.
        """
        with CustomFile(self.filename, 'r') as f:
            f.read()
            f.read()
            self.assertEqual(f.read_counter, 2)

    def test_exception_handling(self):
        """
        Тестування обробки виключень.
        """
        with self.assertRaises(FileNotFoundError):
            with CustomFile('non_existent_file.txt', 'r') as f:
                f.read()

    def test_logging(self):
        """
        Тестування журналу.
        """
        with self.assertLogs(level='INFO') as log:
            with CustomFile(self.filename, 'r') as f:
                f.read()
            self.assertIn(
                'INFO:root:Файл test_file.txt відкрито в режимі r',
                log.output
            )
            self.assertIn(
                'INFO:root:Файл test_file.txt прочитано 1 раз',
                log.output
            )
            self.assertIn(
                'INFO:root:Файл test_file.txt закрито',
                log.output
            )


if __name__ == '__main__':
    unittest.main()
