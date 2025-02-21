# Fibonacci_search
"""Function for performing a Fibonacci search"""


def fibonacci_search(arr, x):
    n = len(arr)

    # Ініціалізація чисел Фібоначчі
    fib_m2 = 0
    fib_m1 = 1
    fib_m = fib_m2 + fib_m1

    # Знаходження найменшого числа Фібоначчі, яке більше або дорівнює n
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    # Зміщення використовується для позначення відрізку в пошуку
    offset = -1

    # Поки є елементи для перевірки
    while fib_m > 1:
        # Перевірка валідності індексу
        i = min(offset + fib_m2, n - 1)

        # Якщо x більше значення на індексі i, перехід до (m-1)-ї підпослідовн.
        if arr[i] < x:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i

        # Якщо x менше значення на індексі i, перехід до (m-2)-ї підпослідовн.
        elif arr[i] > x:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1

        # Якщо x знайдено, повернення індексу
        else:
            return i

    # Порівняння останнього елемента
    if fib_m1 and arr[offset + 1] == x:
        return offset + 1

    # Якщо елемент не знайдено
    return -1


# Приклад використання:
arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
x = 85
index = fibonacci_search(arr, x)

if index != -1:
    print(f"Елемент {x} знайдено у індексі {index}")
else:
    print(f"Елемент {x} не знайдено у масиві")
