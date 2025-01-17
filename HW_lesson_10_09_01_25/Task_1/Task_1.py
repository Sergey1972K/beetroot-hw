# # Task_1

# A function that throws an exception IndexError
def oops():
    raise IndexError("This is an obvious exception IndexError.")


def er_oops():
    try:
        oops()
    except IndexError as e:
        print(f"Exception caught: {e}")

er_oops()

# A function that throws an exception KeyError
def oops():
    raise KeyError("This is an obvious exception KeyError.")


def er_oops():
    try:
        oops()
    except IndexError as e:
        print(f"Exception caught IndexError: {e}")
    except KeyError as e:
        print(f"Exception caught KeyError: {e}")
er_oops()