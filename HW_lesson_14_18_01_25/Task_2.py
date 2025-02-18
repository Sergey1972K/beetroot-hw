# Task_2
# Replacing the list of stop words with * in the decorated function


def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in words:
                result = result.replace(word, '*')
            return result
        return wrapper
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("Steve"))

# Перевірка
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
