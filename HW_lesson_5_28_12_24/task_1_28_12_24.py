# Task 1
# The Guessing Game. Program that generates a random number between 1 and 10

import random

print("Комп'ютер загадає число від 1 до 10. Спробуй вгадати число.")

answer = True
rand = random.randint(1,10)

while answer:
    if answer == False:
        break
    answer = int(input("Число загадане. Спробуй відгадати:"))
    if answer == rand:
        print("Ти вгадав!")
    else:
        print("Ти програв. Спобуй ще!")