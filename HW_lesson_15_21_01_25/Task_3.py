# Task_3
# Prototype tv controller in python

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_idx = 0

    def first_channel(self):
        self.current_idx = 0
        return self.current_channel()

    def last_channel(self):
        self.current_idx = len(self.channels) - 1
        return self.current_channel()

    def turn_channel(self, number):
        if 1 <= number <= len(self.channels):
            self.current_idx = number - 1
        return self.current_channel()

    def next_channel(self):
        self.current_idx = (self.current_idx + 1) % len(self.channels)
        return self.current_channel()

    def previous_channel(self):
        self.current_idx = (self.current_idx - 1) % len(self.channels)
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.current_idx]

    def exists(self, param):
        if isinstance(param, int):
            return "Так" if 1 <= param <= len(self.channels) else "Ні"
        else:
            return "Так" if param in self.channels else "Ні"


CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = TVController(CHANNELS)

print(controller.first_channel())  # "BBC"
print(controller.last_channel())  # "TV1000"
print(controller.turn_channel(1))  # "BBC"
print(controller.next_channel())  # "Discovery"
print(controller.previous_channel())  # "BBC"
print(controller.current_channel())  # "BBC"
print(controller.exists(4))  # "Ні"
# print(controller.exists("BBC"))  # "Так"
