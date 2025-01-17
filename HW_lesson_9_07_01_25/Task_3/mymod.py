# Task 3
# The program counts the lines and characters in the file

 
# The function reads the input file and counts the number of lines in it
def count_lines(name):
    with open(name, 'r') as file:
        lines = file.readlines()
        return len(lines)


# The function reads the input file and counts the number of characters in it
def count_chars(name):
    with open(name, 'r') as file:
        content = file.read()
        return len(content)

# The function calls both counting functions with the given input file name
def test():
    name = input("Введіть ім'я файлу: ")
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"Кількість рядків у файлі '{name}': {lines}")
    print(f"Кількість символів у файлі '{name}': {chars}")

if __name__ == '__main__':
    test()
    