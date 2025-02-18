# Task_1
# How animals talk


class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("гав")


class Cat(Animal):
    def talk(self):
        print("мяу")


def make_animal_talk(animal):
    animal.talk()


# Приклад використання
dog = Dog()
cat = Cat()

make_animal_talk(dog)
make_animal_talk(cat)
