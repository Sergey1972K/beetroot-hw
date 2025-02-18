import unittest
from io import StringIO
import sys
import json

# Імпорт функцій з програми
from phonebook import (
    load_phonebook, save_phonebook, create_contact,
    show_phonebook, search_entry, delete_entry, update_entry
)


class TestPhoneBook(unittest.TestCase):

    def setUp(self):
        self.phonebook = {}
        self.filename = 'test_phonebook.json'

    def tearDown(self):
        import os
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_load_phonebook(self):
        # Тест завантаження неіснуючого файлу
        result = load_phonebook('non_existent.json')
        self.assertEqual(result, {})

    def test_save_phonebook(self):
        # Тест збереження телефонної книги
        save_phonebook(self.filename, self.phonebook)
        with open(self.filename, 'r') as file:
            data = json.load(file)
        self.assertEqual(data, self.phonebook)

    def test_create_contact(self):
        # Тест створення нового контакту
        input_values = [
            'John', 'Doe', 'Edward', '1234567890', 'City', 'Region'
        ]
        output = StringIO()
        sys.stdout = output
        sys.stdin = StringIO('\n'.join(input_values))

        create_contact(self.phonebook)
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

        self.assertIn('1234567890', self.phonebook)
        self.assertEqual(self.phonebook['1234567890']['Ім\'я'], 'John')
        self.assertEqual(self.phonebook['1234567890']['Прізвище'], 'Doe')
        self.assertEqual(self.phonebook['1234567890']['По-батькові'], 'Edward')
        self.assertEqual(self.phonebook['1234567890']['Місто'], 'City')
        self.assertEqual(self.phonebook['1234567890']['Область'], 'Region')

    def test_show_phonebook(self):
        # Тест показу контактів
        self.phonebook['1234567890'] = {
            'Ім\'я': 'John', 'Прізвище': 'Doe', 'По-батькові': 'Edward',
            'Повне ім\'я': 'John Edward Doe', 'Номер телефону': '1234567890',
            'Місто': 'City', 'Область': 'Region'
        }
        output = StringIO()
        sys.stdout = output

        show_phonebook(self.phonebook)
        sys.stdout = sys.__stdout__

        expected_output = 'John Edward Doe - 1234567890 - City, Region\n'
        self.assertEqual(output.getvalue(), expected_output)

    def test_search_entry(self):
        # Тест пошуку запису
        self.phonebook['1234567890'] = {
            'Ім\'я': 'John', 'Прізвище': 'Doe', 'По-батькові': 'Edward',
            'Повне ім\'я': 'John Edward Doe', 'Номер телефону': '1234567890',
            'Місто': 'City', 'Область': 'Region'
        }
        output = StringIO()
        sys.stdout = output

        search_entry(self.phonebook, 'Ім\'я', 'John')
        sys.stdout = sys.__stdout__

        # Use eval to convert the string output to a dictionary
        actual_output = eval(output.getvalue().strip())

        expected_output = {
            'Ім\'я': 'John',
            'Прізвище': 'Doe',
            'По-батькові': 'Edward',
            'Повне ім\'я': 'John Edward Doe',
            'Номер телефону': '1234567890',
            'Місто': 'City',
            'Область': 'Region'
        }

        self.assertEqual(actual_output, expected_output)

    def test_delete_entry(self):
        # Тест видалення запису
        self.phonebook['1234567890'] = {
            'Ім\'я': 'John', 'Прізвище': 'Doe', 'По-батькові': 'Edward',
            'Повне ім\'я': 'John Edward Doe', 'Номер телефону': '1234567890',
            'Місто': 'City', 'Область': 'Region'
        }
        delete_entry(self.phonebook, '1234567890')
        self.assertNotIn('1234567890', self.phonebook)

    def test_update_entry(self):
        # Тест оновлення запису
        self.phonebook['1234567890'] = {
            'Ім\'я': 'John', 'Прізвище': 'Doe', 'По-батькові': 'Edward',
            'Повне ім\'я': 'John Edward Doe', 'Номер телефону': '1234567890',
            'Місто': 'City', 'Область': 'Region'
        }
        input_values = [
            'Jane', 'Smith', 'Eliza', 'New City', 'New Region'
        ]
        sys.stdin = StringIO('\n'.join(input_values))

        update_entry(self.phonebook, '1234567890')
        sys.stdin = sys.__stdin__

        self.assertEqual(self.phonebook['1234567890']['Ім\'я'], 'Jane')
        self.assertEqual(self.phonebook['1234567890']['Прізвище'], 'Smith')
        self.assertEqual(self.phonebook['1234567890']['По-батькові'], 'Eliza')
        self.assertEqual(self.phonebook['1234567890']['Місто'], 'New City')
        self.assertEqual(self.phonebook['1234567890']['Область'], 'New Region')

    def test_create_duplicate_contact(self):
        # Тест створення дублюючого контакту
        input_values = [
            'John', 'Doe', 'Edward', '1234567890', 'City', 'Region'
        ]
        sys.stdin = StringIO('\n'.join(input_values))
        create_contact(self.phonebook)
        sys.stdin = sys.__stdin__

        input_values = [
            'John', 'Doe', 'Edward', '1234567890', 'City', 'Region'
        ]
        sys.stdin = StringIO('\n'.join(input_values))
        create_contact(self.phonebook)
        sys.stdin = sys.__stdin__

        self.assertEqual(len(self.phonebook), 1)
        self.assertEqual(self.phonebook['1234567890']['Ім\'я'], 'John')

    def test_update_non_existent_entry(self):
        # Тест оновлення неіснуючого запису
        input_values = [
            'Jane', 'Smith', 'Eliza', 'New City', 'New Region'
        ]
        sys.stdin = StringIO('\n'.join(input_values))
        update_entry(self.phonebook, '0000000000')
        sys.stdin = sys.__stdin__

        self.assertNotIn('0000000000', self.phonebook)


if __name__ == "__main__":
    unittest.main()
