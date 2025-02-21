# Medium_level
"""Implement in (__contains__) and len (__len__) methods
   for HashTableMiddle level
"""


class HashTable:
    def __init__(self):
        self.table = {}
        self.size = 0

    def __setitem__(self, key, value):
        # Якщо ключа немає у таблиці, збільшуємо розмір
        if key not in self.table:
            self.size += 1
        self.table[key] = value

    def __getitem__(self, key):
        # Повертаємо значення за ключем
        return self.table[key]

    def __delitem__(self, key):
        # Видаляємо ключ з таблиці і зменшуємо розмір, якщо ключ існує
        if key in self.table:
            self.size -= 1
            del self.table[key]

    def __contains__(self, key):
        # Перевірка наявності ключа у хеш-таблиці.
        return key in self.table

    def __len__(self):
        # Повертає кількість елементів у хеш-таблиці.
        return self.size


# Приклад використання:
hash_table = HashTable()
hash_table["apple"] = 10
hash_table["banana"] = 20

# Перевірка наявності ключа у хеш-таблиці
print("apple" in hash_table)  # True
print("orange" in hash_table)  # False

# Повертає кількість елементів у хеш-таблиці
print(len(hash_table))  # 2
