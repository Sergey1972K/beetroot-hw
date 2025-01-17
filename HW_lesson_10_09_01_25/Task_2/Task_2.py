# Task_2
# function calls the numbers a and b , and then returns the square of a divided by b

def calculate():
    try:
        a = float(input("Число а: "))
        b = float(input("Число b: "))
        result = (a ** 2) / b
        return result
    except ZeroDivisionError:
        return "Ділити на нуль неможливо."
    except ValueError:
        return "Значення повинні бути числами."
result = calculate()
print(result)
