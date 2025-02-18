# Task_1
"""A program that reads a sequence of characters and prints them in
   reverse order using a stack implementation
"""


class Stack:
    def __init__(self):
        self.items = []
        # Ініціалізація порожнього стеку

    def is_empty(self):
        return self.items == []
        # Перевірка, чи стек порожній

    def push(self, item):
        self.items.append(item)
        # Додавання елемента у стек

    def pop(self):
        return self.items.pop()
        # Видалення елемента зі стеку

    def peek(self):
        return self.items[-1]
        # Повертає верхній елемент зі стеку без його видалення

    def size(self):
        return len(self.items)
        # Повертає кількість елементів у стеку


def main():
    # Читання послідовності символів
    sequence = input("Введіть послідовність символів: ")

    # Створення стеку
    stack = Stack()

    # Збереження символів у стеку
    for char in sequence:
        stack.push(char)

    # Виведення символів у зворотному порядку
    reversed_sequence = ""
    while not stack.is_empty():
        reversed_sequence += stack.pop()

    print("Послідовність у зворотному порядку:", reversed_sequence)


if __name__ == "__main__":
    main()
    # Виконання основної функції при запуску скрипта
