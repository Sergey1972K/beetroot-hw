# Task_1
# Determining the number of local variables declared in a function.


def my_function():
    a = 2
    b = 4
    c = 6
    d = 8
    return a + b + c + d

num_locals = my_function.__code__.co_nlocals
print(num_locals)
