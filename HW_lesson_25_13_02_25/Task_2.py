# Task_2
"""Implement a stack using a singly linked list."""


class Node:
    """Клас вузла однозв'язаного списку."""

    def __init__(self, value):
        """Ініціалізує вузол з даним значенням."""
        self.value = value
        self.next = None


class Stack:
    """Клас стека на базі однозв'язаного списку."""

    def __init__(self):
        """Ініціалізує порожній стек."""
        self.head = None

    def is_empty(self):
        """Перевіряє, чи є стек порожнім.

        Повертає:
            bool: True, якщо стек порожній, інакше False.
        """
        return self.head is None

    def push(self, value):
        """Додає новий елемент до стека.

        Аргументи:
            value: Значення, яке потрібно додати до стека.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """Видаляє і повертає верхній елемент стека.

        Повертає:
            value: Значення верхнього елемента.

        Піднімає:
            IndexError: Якщо стек порожній.
        """
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self):
        """Повертає значення верхнього елемента стека без видалення.

        Повертає:
            value: Значення верхнього елемента.

        Піднімає:
            IndexError: Якщо стек порожній.
        """
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.head.value

    def __str__(self):
        """Повертає рядкове представлення стека.

        Повертає:
            str: Рядкове представлення стека.
        """
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return ' -> '.join(map(str, result))


# Приклад використання:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack)  # Виведе: 30 -> 20 -> 10
print(stack.pop())  # Виведе: 30
print(stack.peek())  # Виведе: 20
print(stack)  # Виведе: 20 -> 10
