# Task_3
"""Extend the Stack to include a method called get_from_stack that searches 
   and returns an element e from a stack. Any other element must remain on 
   the stack respecting their order. Consider the case in which the element 
   is not found - raise ValueError with proper info Message
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
        if self.is_empty():
            return None
        return self.items.pop()
        # Видалення елемента зі стеку

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
        # Повертає верхній елемент зі стеку без його видалення

    def size(self):
        return len(self.items)
        # Повертає кількість елементів у стеку

    def get_from_stack(self, e):
        temp_stack = Stack()
        found = False

        # Шукаємо елемент і переміщуємо елементи до тимчасового стеку
        while not self.is_empty():
            item = self.pop()
            if item == e:
                found = True
                break
            temp_stack.push(item)

        # Повертаємо елементи назад до оригінального стеку
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if not found:
            raise ValueError(f"Елемент {e} не знайдено у стеку")

        return e
        # Повертає елемент e, якщо його знайдено у стеку


def main():
    stack = Stack()
    sequence = [1, 2, 3, 4, 5]

    for item in sequence:
        stack.push(item)

    try:
        element = stack.get_from_stack(3)
        print(f"Знайдено елемент: {element}")
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
    # Виконання основної функції при запуску скрипта
