from string import ascii_uppercase, digits
import random as r


def robo_name():
    letters = ''.join(r.choices(ascii_uppercase, k = 2))
    numbers = ''.join(r.choices(digits, k = 3))

    name = letters + numbers

    return name

class Robot:
    def __init__(self):
        self.name = self.robo()

    def robo(self):
        return robo_name()

    def reset(self):
        self.name = self.robo() if self.robo() != robo_name() else robo_name()
