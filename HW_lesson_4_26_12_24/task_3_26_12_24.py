# Task 3
#  Program that asks the answer for a mathematical expression 
#  Program checks whether the user is right or wrong, and then responds with a message accordingly.

import random

def generate_question():
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice(operations)
    if op == '+':
        answer = num1 + num2
    elif op == '-':
        answer = num1 - num2
    elif op == '*':
        answer = num1 * num2
    elif op == '/':
        answer = num1 / num2
    question = f"{num1} {op} {num2}"
    return question, round(answer, 2) 
def math_quiz():
    question, correct_answer = generate_question()

    print(f"Розв’яжіть: {question}")

    try:
        user_answer = float(input("Ваша відповідь: "))

        if user_answer == correct_answer:
            print("Правильно")
        else:
            print(f"Неправильно. Правильна відповідь: {correct_answer}.")
    except ValueError:
        print("Введіть числове значення.")

if __name__ == "__main__":
    math_quiz()