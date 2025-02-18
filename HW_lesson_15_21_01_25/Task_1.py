# Task_1
# A class called Person


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        print(f"""Привіт, мене звати {self.first_name} {self.last_name},
              мені {self.age} років.""")


person = Person("Сергій", "Клен", 52)
person.talk()
