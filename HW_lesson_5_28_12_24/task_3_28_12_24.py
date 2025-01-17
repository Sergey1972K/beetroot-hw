# Task 3
# Program that reads an input string and then creates and prints 5 random strings

import random

data = input("Enter string :")
def random_string(input_string): 
    return ''.join(random.sample(input_string, len(input_string)))
for i in range(5):
    print(f"Відповідь:{random_string(data)}")
       