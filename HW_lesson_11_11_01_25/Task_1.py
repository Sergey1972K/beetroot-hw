# myscript.py
def greet(name):
    print(f"Привіт, {name}!")

greet("Софія")

if __name__ == "__main__":
    name = input("Введіть ваше ім'я: ")
    greet(name)