# Task_2
"""A program that reads a sequence of characters and determines whether
   parentheses, parentheses, and curly braces are "balanced.
"""


def is_balanced(sequence):
    # Ініціалізуємо стек для зберігання відкривних дужок
    stack = []
    # Набір відкривних дужок
    opening = "({["
    # Набір закривних дужок
    closing = ")}]"
    # Відповідність між відкривними і закривними дужками
    mapping = {")": "(", "}": "{", "]": "["}

    for char in sequence:
        # Якщо символ є відкривною дужкою, додаємо його до стека
        if char in opening:
            stack.append(char)
        # Якщо символ є закривною дужкою
        elif char in closing:
            # Перевіряємо, чи не порожній стек і чи відповідає остання відкривна дужка
            if not stack or stack[-1] != mapping[char]:
                return False
            # Видаляємо останню відкривну дужку зі стека
            stack.pop()

    # Якщо стек порожній після перевірки всіх дужок, вони збалансовані
    return not stack


def main():
    # Запитуємо у користувача ввести послідовність символів
    sequence = input("Введіть послідовність символів: ")
    # Перевіряємо, чи збалансовані дужки
    if is_balanced(sequence):
        print("Дужки збалансовані.")
    else:
        print("Дужки не збалансовані.")


if __name__ == "__main__":
    main()
