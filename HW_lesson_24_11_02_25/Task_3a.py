# Task_3
"""Extend the Queue to include a method called get_from_stack that searches 
   and returns an element e from a queue. Any other element must remain in 
   the queue respecting their order. Consider the case in which the element 
   is not found - raise ValueError with proper info Message
"""


class Queue:
    def __init__(self):
        self.items = []
        # Ініціалізація порожньої черги

    def is_empty(self):
        return self.items == []
        # Перевірка, чи черга порожня

    def enqueue(self, item):
        self.items.insert(0, item)
        # Додавання елемента до черги

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop()
        # Видалення елемента з черги

    def size(self):
        return len(self.items)
        # Повертає кількість елементів у черзі

    def get_from_queue(self, e):
        temp_queue = []
        found = False

        # Шукаємо елемент і переміщуємо елементи до тимчасового списку
        while not self.is_empty():
            item = self.dequeue()
            if item == e:
                found = True
                break
            temp_queue.append(item)
            # Якщо елемент знайдено, встановлюємо прапорець і виходимо з циклу

        # Повертаємо елементи назад до оригінальної черги
        while temp_queue:
            self.enqueue(temp_queue.pop(0))
            # Додаємо елементи назад у чергу

        if not found:
            raise ValueError(f"Елемент {e} не знайдено у черзі")
            # Якщо елемент не знайдено, викликаємо виняток ValueError

        return e
        # Повертає елемент e, якщо його знайдено у черзі


def main():
    queue = Queue()
    sequence = [1, 2, 3, 4, 5]

    for item in sequence:
        queue.enqueue(item)
        # Додаємо елементи з послідовності до черги

    try:
        element = queue.get_from_queue(3)
        print(f"Знайдено елемент: {element}")
        # Пошук елемента у черзі та виведення результату
    except ValueError as error:
        print(error)
        # Обробка винятку, якщо елемент не знайдено


if __name__ == "__main__":
    main()
    # Виконання основної функції при запуску скрипта
