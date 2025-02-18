# Task_1
"""
Pick your solution to one of the exercises in this module.
Design tests for this solution and write tests using unittest library.

Task 2
Doggy age
Create a class Dog with class attribute 'age_factor' equals to 7.
Make __init__() which takes values for a dog’s age. Then create a method
`human_age` which returns the dog’s age in human equivalent.
"""


import unittest


class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * self.age_factor


class TestDog(unittest.TestCase):

    def setUp(self):
        self.dog = Dog(12)

    def test_human_age(self):
        self.assertEqual(self.dog.human_age(), 84)

    def test_age_factor(self):
        self.assertEqual(self.dog.age_factor, 7)

    def test_age_initialization(self):
        self.assertEqual(self.dog.age, 12)


if __name__ == '__main__':
    unittest.main()
