# Task_3
# A decorator that checks the arguments of the passed function


def arg_rules(type_, max_length, contains):
    def decorator(func):
        def wrapper(arg):
            if not isinstance(arg, type_):
                print(f"Error: Argument should be of type {type_}")
                return False
            if len(arg) > max_length:
                print(f"Error: Argument should not exceed {max_length}"
                      f"characters")
                return False
            for char in contains:
                if char not in arg:
                    print(f"Error: Argument should contain '{char}'")
                    return False
            return func(arg)
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name):
    return f"{name} drinks Pepsi in his brand new BMW!"


# перевірка
print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('JohnDoe05@'))
print(create_slogan('JaneDoe'))
print(create_slogan('S@SH05'))
