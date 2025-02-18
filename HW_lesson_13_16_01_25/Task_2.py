# Task_2
# program to access a function inside a function


def traffic_sign(sign):
    def sign_berd(kilometer):
        return kilometer * sign
    return sign_berd


distance = traffic_sign(235)
print(distance(2))
