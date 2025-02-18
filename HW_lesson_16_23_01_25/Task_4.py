# Task_4
# Exception writes error messages to the "logs.txt" file.


class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.log_error(msg)

    def log_error(self, msg):
        with open("logs.txt", "a") as log_file:
            log_file.write(f"{msg}\n")


# Приклад використання
try:
    raise CustomException("Це повідомлення про помилку")
except CustomException as e:
    print(e)
