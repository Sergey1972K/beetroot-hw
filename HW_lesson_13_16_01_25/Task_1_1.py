# Task_1
# Determining the number of local variables declared in a function.

def my_function():
    a = 2
    b = 4
    c = 6
    d = 8
    local_vars = locals()
    return len(local_vars)
print(my_function())