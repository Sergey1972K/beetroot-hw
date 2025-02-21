# Binary_search
"""Implementation of a binary search algorithm using recursion"""


def binary_search_recursive(arr, low, high, x):
    if high >= low:
        mid = low + (high - low) // 2

        # Якщо x знаходиться на середньому індексі
        if arr[mid] == x:
            return mid

        # Якщо x менший за середній елем., рекурсивно шукаємо у лівій половині
        if arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)

        # Якщо x більший за середній ел., рекурсивно шукаємо у правій половині
        return binary_search_recursive(arr, mid + 1, high, x)

    # Якщо елемент не знайдено
    return -1


# Приклад використання:
arr = [2, 3, 4, 10, 40]
x = 10

# Викликаємо функцію з початковими значеннями low і high
result = binary_search_recursive(arr, 0, len(arr) - 1, x)

if result != -1:
    print(f"Елемент {x} знайдено у індексі {result}")
else:
    print(f"Елемент {x} не знайдено у масиві")
