# Task_3
"""Implement a queue using a singly linked list."""


class Node:
    """Клас вузла однозв'язаного списку."""

    def __init__(self, value):
        """Ініціалізує вузол з даним значенням."""
        self.value = value
        self.next = None


class Queue:
    """Клас черги на базі однозв'язаного списку."""

    def __init__(self):
        """Ініціалізує порожню чергу."""
        self.front = None
        self.rear = None

    def is_empty(self):
        """Перевіряє, чи є черга порожньою.

        Повертає:
            bool: True, якщо черга порожня, інакше False.
        """
        return self.front is None

    def enqueue(self, value):
        """Додає новий елемент до кінця черги.

        Аргументи:
            value: Значення, яке потрібно додати до черги.
        """
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """Видаляє і повертає елемент з початку черги.

        Повертає:
            value: Значення елемента з початку черги.

        Піднімає:
            IndexError: Якщо черга порожня.
        """
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        """Повертає значення елемента з початку черги без видалення.

        Повертає:
            value: Значення елемента з початку черги.

        Піднімає:
            IndexError: Якщо черга порожня.
        """
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self.front.value

    def __str__(self):
        """Повертає рядкове представлення черги.

        Повертає:
            str: Рядкове представлення черги.
        """
        result = []
        current = self.front
        while current:
            result.append(current.value)
            current = current.next
        return ' -> '.join(map(str, result))


# Приклад використання:
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue)  # Виведе: 10 -> 20 -> 30
print(queue.dequeue())  # Виведе: 10
print(queue.peek())  # Виведе: 20
print(queue)  # Виведе: 20 -> 30
