# Task_3
# Iterable for a for-in loop


class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < len(self.data):
            result = self.data[self.current_index]
            self.current_index += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError('Index out of range')
        return self.data[index]


# Використання
my_iterable = MyIterable([1, 2, 3, 4, 5])

# Використання в циклі for-in
for item in my_iterable:
    print(item)

# За допомогою квадратних дужок
print(my_iterable[2])
print(my_iterable[4])
