# Task 2
# Exclusive common numbers.

import random

list1 = []
list2 = []

i = 0
while i < 10:
    list1.append(random.randint(1, 10))
    i += 1

i = 0
while i < 10:
    list2.append(random.randint(1, 10))
    i += 1

common_numbers = []
i = 0
while i < len(list1):
    num = list1[i]
    if num in list2 and num not in common_numbers:
        common_numbers.append(num)
    i += 1

print("Перший список:", list1)
print("Другий список:", list2)
print("Загальні числа:", common_numbers)