# Task_3
"""
    Функція приймає об'єкт файлу, читає текстові дані та підраховує кількість
    рядків, слів та символів.
"""


def test_check(file_obj):
    lines = file_obj.readlines()
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)

    # Друк результатів
    print(f"Кількість рядків: {len(lines)}")
    print(f"Кількість слів: {word_count}")
    print(f"Кількість символів: {char_count}")

    return len(lines), word_count, char_count


# Відкрийте файл для читання
if __name__ == '__main__':
    with open('example.txt', 'r', encoding='utf-8') as file:
        test_check(file)
