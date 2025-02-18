# Task_1
""" Create your own class, which can behave like a built-in function 'open'.
    Also, you need to extend its functionality with counter and logging.
    Pay special attention to the implementation of '__exit__' method,
    which has to cover all the requirements to context managers mentioned here.
"""


import logging

# Налаштовуємо базову конфігурацію logging для виведення інформації
logging.basicConfig(level=logging.INFO)


class CustomFile:
    def __init__(self, filename, mode):
        """
        Ініціалізуємо ім'я файлу, режим, об'єкт файлу та лічильник читань.
        """
        self.filename = filename
        self.mode = mode
        self.file = None
        self.read_counter = 0

    def __enter__(self):
        """
        Відкриваємо файл у заданому режимі, ведемо журнал про відкриття файлу.
        """
        self.file = open(self.filename, self.mode)
        logging.info(f"Файл {self.filename} відкрито в режимі {self.mode}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Закриваємо файл, якщо він відкритий,  ведемо журнал про закриття файлу.
        Обробляємо виключення, якщо вони виникають.
        """
        if self.file:
            self.file.close()
            logging.info(f"Файл {self.filename} закрито")
        if exc_type:
            logging.error(f"Виникла помилка: {exc_type}, {exc_val}")
        return True  # Повертаючи True, ми запобігаємо перекидання винятку

    def read(self):
        """
        Читаємо дані з файлу, збільшуємо лічильник читань, ведемо журнал про це
        """
        data = self.file.read()
        self.read_counter += 1
        logging.info(f"Файл {self.filename} прочитано {self.read_counter} раз")
        return data

    def write(self, data):
        """
        Записуємо дані у файл і ведемо журнал про це.
        """
        self.file.write(data)
        logging.info(f"Дані записані у файл {self.filename}")


# Використання нашого класу для запису даних у файл
with CustomFile('example.txt', 'w') as f:
    f.write('Мене звати Сергій')

# Використання нашого класу для читання даних з файлу
with CustomFile('example.txt', 'r') as f:
    content = f.read()
    print(content)
