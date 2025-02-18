# Task_3
# TypeDecorators class to convert function results to the specified type

from functools import wraps


class TypeDecorators:
    """Клас, який містить статичні методи для перетворення результатів функцій
       у вказаний тип."""

    @staticmethod
    def to_int(func):
        """Декоратор для перетворення результату функції у ціле число."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return int(result) if result.isdigit() else None
        return wrapper

    @staticmethod
    def to_str(func):
        """Декоратор для перетворення результату функції у рядок."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)
        return wrapper

    @staticmethod
    def to_bool(func):
        """Декоратор для перетворення результату функції у булеве значення."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return (result.lower() in ['true', '1', 'yes']
                    if isinstance(result, str)
                    else bool(result))
        return wrapper

    @staticmethod
    def to_float(func):
        """Декоратор для перетворення результату функції у число з плаваючою
           комою."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except ValueError:
                return None
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    """Функція, яка нічого не робить і повертає вхідний рядок."""
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    """Функція, яка нічого не робить і повертає вхідний рядок."""
    return string


# Тестові випадки
assert do_nothing('25') == 25
assert do_something('True') is True
assert do_something('false') is False
