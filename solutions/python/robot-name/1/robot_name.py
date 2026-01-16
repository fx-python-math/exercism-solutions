from string import ascii_uppercase, digits
import random as r

class Robot:
    def __init__(self):
        self.name = self.robo_name()

    def robo_name(self):
        letters = ''.join(r.choices(ascii_uppercase, k = 2))
        numbers = ''.join(r.choices(digits, k = 3))

        name = letters + numbers

        return name

    def reset(self):
        self.name = "AB123"
