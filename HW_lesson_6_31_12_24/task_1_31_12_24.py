# Tesk 1
# largest number from the list of random numbers
# Generate 10 random numbers in the range from 1 to 100

import random

line = " ".join(str(random.randint(1, 100)) for _ in range(10))

print("Рядок чисел:", line)

numbers = line.split()
i = 0
max_number = int(numbers[0]) 

while i < len(numbers):
    current_number = int(numbers[i])  
    if current_number > max_number:  
        max_number = current_number
    i += 1  

print("Найбільше число в рядку:", max_number)