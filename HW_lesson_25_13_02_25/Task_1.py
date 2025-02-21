# Task_1
"""Implement append, index, pop, insert methods for UnsortedList.
   Also implement a slice method, which will take two parameters 'start' and
   'stop', and return a copy of the list starting at the position and going
   up to but not including the stop position.
"""


class UnsortedList:
    def __init__(self):
        """Ініціалізує порожній список"""
        self.items = []

    def append(self, item):
        """Додає елемент до кінця списку"""
        self.items.append(item)

    def index(self, item):
        """
        Повертає індекс першого входження елемента у списку.
        Якщо елемент не знайдено, повертає -1.
        """
        for i in range(len(self.items)):
            if self.items[i] == item:
                return i
        return -1

    def pop(self, index=None):
        """
        Видаляє та повертає елемент з кінця списку або за заданим індексом.
        Якщо індекс не вказано, видаляє та повертає останній елемент.
        """
        if index is None:
            return self.items.pop()
        else:
            if 0 <= index < len(self.items):
                return self.items.pop(index)
            else:
                raise IndexError("pop index out of range")

    def insert(self, index, item):
        """
        Вставляє елемент на задану позицію у списку.
        """
        if 0 <= index <= len(self.items):
            self.items.insert(index, item)
        else:
            raise IndexError("insert index out of range")

    def slice(self, start, stop):
        """
        Повертає копію списку від індексу 'start' до індексу `stop'
        """
        return self.items[start:stop]


# Приклад використання:
lst = UnsortedList()
lst.append(1)
lst.append(2)
lst.append(3)
print(lst.items)       # [1, 2, 3]

lst.insert(1, 4)
print(lst.items)       # [1, 4, 2, 3]

print(lst.index(4))    # 1

lst.pop(1)
print(lst.items)       # [1, 2, 3]
print(lst.slice(1, 3)) # [2, 3]
