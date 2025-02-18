# Task_2
# Range function


def in_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start

    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    elif step < 0:
        while current > stop:
            yield current
            current += step
    else:
        raise ValueError("step must not be zero")


# Приклад використання
print(list(in_range(5)))           # [0, 1, 2, 3, 4]
print(list(in_range(1, 5)))        # [1, 2, 3, 4]
print(list(in_range(1, 10, 2)))    # [1, 3, 5, 7, 9]
print(list(in_range(10, 1, -2)))   # [10, 8, 6, 4, 2]
