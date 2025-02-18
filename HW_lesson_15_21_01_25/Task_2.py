# Task_2
# The ratio of the dog's age to the human age


class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * self.age_factor


dog = Dog(12)
print(f"The human equivalent age of the dog is: {dog.human_age()} years.")
