# Task_1
# A class method called `validate` to validate the parameter's email


import re


class EmailValidator:
    def __init__(self, email):
        self.email = email
        self.validate()

    def validate(self):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(pattern, self.email):
            raise ValueError(f"'{self.email}' is not a valid email address")


try:
    email = EmailValidator("sergey@domain.com")
    print("Email is valid")
except ValueError as e:
    print(e)
