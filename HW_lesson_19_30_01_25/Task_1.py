# Task_1
# Custom enumerate function


def with_index(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1


# Використання
my_list = ['a', 'b', 'c', 'd']
for index, value in with_index(my_list, start=1):
    print(f"Index: {index}, Value: {value}")
