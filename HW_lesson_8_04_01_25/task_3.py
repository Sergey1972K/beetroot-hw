# Task 3 
# A simple calculator

def make_operation(operator,  args ):
    if operator == "+":
        result = sum(args)
    elif operator == "-":
        result = args[0]
        for num in args[1:]:
            result -= num
    elif operator == "*":
        result = 1
        for num in args:
            result = num
    else:
        raise ValueError("Use '+', '-', or '*'.")

    return result