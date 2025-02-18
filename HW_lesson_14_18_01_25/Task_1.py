# Task_1
# A decorator that prints the function with the arguments passed to it

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args}"
              f"and keyword arguments {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


# перевірка
add(4, 5)
square_all(2, 3, 4)
