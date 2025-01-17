# Task 3
# list that contains all integers from 1 to 100 that are divisible by 7 but not a multiple of 5

data = 1
while data <= 100:
    data = data + 1
    if (data%7==0 and data%5!=0):
        print(data)
        